from rest_framework.response import Response
from rest_framework import viewsets, status
from users.models import *
from users.serializers import (
                            UserSerializer, 
                            LoginSerializer, 
                            LogOutSerializer, 
                            AllUserDataSerializer, 
                            ChangePasswordSerializer,
                            RequestSerializer
)
from django.shortcuts import get_object_or_404
import jwt, datetime


# swagger_setting_input_fields
# @swagger_auto_schema(operation_summary="info", request_body=Serializer)
from drf_yasg.utils import swagger_auto_schema


# email 
from django.core.mail import send_mail
from django.conf import settings


# class TestViewSet(viewsets.ModelViewSet):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer
    
#     list_ = [1, 2, 3, 4]
    
#     def get_list(self, request, name : str):
#         # return Response(data=self.list_, status=status.HTTP_200_OK)
#         return Response(data=name)
    
#     def post_req(self, request):
#         data = request.data['age']
#         return Response(data=data)


def checkAuthentication(request) -> Response:
    token = request.COOKIES.get('jwt')
        
    if not token:
        return Response(data={"permission" : "denied"})
    
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return Response(data={"permission" : "denied"})
    user_id = payload['id']
    
    user = User.objects.filter(pk=user_id)[0]
    serializer = AllUserDataSerializer(instance=user)
    
    return Response(data=serializer.data)

def isAdmin(request) -> bool:
    try:
        user = checkAuthentication(request)
        return user.data.get('user_type') == 'Admin'
    except:
        return False
        
        

def isCustomer(request) -> bool:
    try:
        user = checkAuthentication(request)
        if user.data.get('user_type') == 'Customer':
            return True
        return False
    except:
        return False

def isOwner(request) -> bool:
    try:
        user = checkAuthentication(request)
        if user.data.get('user_type') == 'Owner':
            return True
        return False
    except:
        return False

def isAuthenticated(request):
    return checkAuthentication(request).data != {"permission" : "denied"}


class AuthorizationViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    
    # post 
    @swagger_auto_schema(operation_summary="join to the system", request_body=LoginSerializer)
    def login(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response(data= {"detail" : "does not correct password"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(instance=user)
        
        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.data={"token" : token, "user" : serializer.data}
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response

    # post
    def signup(self, request):
        if request.data['user_type'] == 'Admin':
            return Response(data={"detail" : "permission denied"})
        
        serilalizer = UserSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            user = User.objects.filter(username=request.data["username"])[0]
            
            user.set_password(request.data["password"])
            user.save()
            anotherSerializer = UserSerializer(instance=user)
            return Response({"token" : 1, "user" : anotherSerializer.data}, status=status.HTTP_200_OK)
        return Response(serilalizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get 
    # def test(self, request):
    #     response = checkAuthentication(request=request)
    #     # response.data['password'] = 'krutoi'
    #     return response

    # post 
    @swagger_auto_schema(operation_summary="exit", request_body=LogOutSerializer)
    def logout(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'status' : 'success'}
        return response
    
    def get_user(cls, request):
        
        if request.headers.get('Authorization', ''):
            token = request.headers.get('Authorization', '')
            try:
                payload = jwt.decode(token, 'secret', algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return Response(data={"permission" : "denied"})
            user_id = payload['id']
            user = User.objects.filter(pk=user_id)[0]
            serializer = AllUserDataSerializer(instance=user)
            return Response(data=serializer.data)
        else:
            param = request.query_params.get('id')
            user = User.objects.filter(pk=param)[0]
            serializer = AllUserDataSerializer(instance=user)
            return Response(data=serializer.data)
        # return checkAuthentication(request)
        # return Response(data=isAuthenticated(request))

    @swagger_auto_schema(operation_summary="change password", request_body=ChangePasswordSerializer)
    def change_password(cls, request):
        
        try:
            id = request.data.get('id')
            user = User.objects.get(pk=id)
            user.set_password(request.data['password'])
            user.save()
            return Response(data={'status' : 'success'})
        except:
            return Response(data={"detail" : "permission denied"})
            

class RequestViewSet(viewsets.ModelViewSet):
    
    @swagger_auto_schema(operation_summary="request sending", request_body=RequestSerializer)
    def send_request(cls, request):
        # pass
        serilizer = RequestSerializer(data=request.data)
        if serilizer.is_valid():
            request = serilizer.save() # сатегория requset.category описание requset.description requset.email  тема requset.subject
            send_mail('Тема: ', request.description, settings.EMAIL_HOST_USER, [request.email]) # Вот функция отправки сообщений на почту
            return Response(data={'status' : 'success'})
        else:
            return Response(data=serilizer.errors)
    # delete
    def delete_request(self, request, id):
        if not isAdmin(request): return Response({"detail" : "Нет доступа"})
        try:
            request = Request.objects.get(pk=id)
            request.delete()
        except:
            return Response({"detail" : "Not Found"})
        return Response({"detail" : "success"})
    #get
    def get_requests_byEmail(self, request):
        email = request.query_params.get('email')
        if email:
            queryset = Request.objects.filter(email=email)
        else:
            return Response({"error": "Email не распознан."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = RequestSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    def get_requests(self, request):
        if not isAdmin(request): return Response({"detail" : "Нет доступа"})
        queryset = Request.objects.all()
        serializer = RequestSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)