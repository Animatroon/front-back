from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import (Catalog,
                     Reestr,
                     PoiskPravoobladateley,
                     InostrannyeOkupy,
                     SubReestr
                     )
from .serializers import (CatalogSerializer,
                          ReestrSerializer, 
                          PoiskPravoobladateleySerializer,
                          InostrannyeOkupySerializer,
                          SubReestrSerializer
                          )
from django.shortcuts import get_object_or_404


# permissions 
from users.views import isAdmin, isCustomer, isOwner, isAuthenticated, checkAuthentication

from drf_yasg.utils import swagger_auto_schema

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
    # get
    def get_all_catalogs(self, request):
        queryset = Catalog.objects.all()
        serializer = CatalogSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_catalog(self, request, pk):
        catalog = Catalog.objects.filter(pk=pk)[0]
        serializer = CatalogSerializer(instance=catalog)
        return Response(data=serializer.data)
    
    # patch 
    def change_catalog(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        catalog = Catalog.objects.filter(pk=request.data['id'])[0]
        catalog.name = request.data['name']
        if (not request.data.get('file', True)) and catalog.file != request.data['file']:
            catalog.file = request.data['file']
        catalog.save()
        serializer = CatalogSerializer(instance=catalog)
        return Response(serializer.data)

    # delete 
    def delete_catalog(self, request, pk):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        catalog = Catalog.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_catalog(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        serializer = CatalogSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    

class ReestrViewSet(viewsets.ModelViewSet):
    queryset = Reestr.objects.all()
    serializer_class = ReestrSerializer
    
    # get
    def get_all_reestrs(self, request):
        queryset = Reestr.objects.all()
        serializer = ReestrSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_reestr(self, request, pk):
        reestr = Reestr.objects.filter(pk=pk)[0]
        serializer = ReestrSerializer(instance=reestr)
        return Response(data=serializer.data)
    
    # patch 
    def change_reestr(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        reestr = Reestr.objects.filter(pk=request.data['id'])[0]
        reestr.name = request.data['name']
        if (not request.data.get('file', True)) and reestr.file != request.data['file']:
            reestr.file = request.data['file']
        reestr.save()
        serializer = ReestrSerializer(instance=reestr)
        return Response(serializer.data)

    # delete 
    def delete_reestr(self, request, pk):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        reestr = Reestr.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_reestr(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        serializer = ReestrSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    


class PoiskPravoobladateleyViewSet(viewsets.ModelViewSet):
    queryset = PoiskPravoobladateley.objects.all()
    serializer_class = ReestrSerializer
    
    # get
    def get_all_poisk_pravoobladateleys(self, request):
        queryset = PoiskPravoobladateley.objects.all()
        serializer = PoiskPravoobladateleySerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_poisk_pravoobladateley(self, request, pk):
        poisk_pravoobladateley = PoiskPravoobladateley.objects.filter(pk=pk)[0]
        serializer = PoiskPravoobladateleySerializer(instance=poisk_pravoobladateley)
        return Response(data=serializer.data)
    
    # patch 
    def change_poisk_pravoobladateley(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        poisk_pravoobladateley = PoiskPravoobladateley.objects.filter(pk=request.data['id'])[0]
        poisk_pravoobladateley.name = request.data['name']
        if (not request.data.get('file', True)) and poisk_pravoobladateley.file != request.data['file']:
            poisk_pravoobladateley.file = request.data['file']
        poisk_pravoobladateley.save()
        serializer = PoiskPravoobladateleySerializer(instance=poisk_pravoobladateley)
        return Response(serializer.data)

    # delete 
    def delete_poisk_pravoobladateley(self, request, pk):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        poisk_pravoobladateley = PoiskPravoobladateley.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_poisk_pravoobladateley(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        serializer = PoiskPravoobladateleySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)



class InostrannyeOkupyViewSet(viewsets.ModelViewSet):
    queryset = InostrannyeOkupy.objects.all()
    serializer_class = InostrannyeOkupySerializer
    
    # get
    def get_all_inostrannye_okupys(self, request):
        queryset = InostrannyeOkupy.objects.all()
        serializer = InostrannyeOkupySerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_inostrannye_okupy(self, request, pk):
        inostrannye_okupy = InostrannyeOkupy.objects.filter(pk=pk)[0]
        serializer = InostrannyeOkupySerializer(instance=inostrannye_okupy)
        return Response(data=serializer.data)
    
    # patch 
    def change_inostrannye_okupy(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        inostrannye_okupy = InostrannyeOkupy.objects.filter(pk=request.data['id'])[0]
        inostrannye_okupy.title = request.data['title']
        inostrannye_okupy.text = request.data['text']
        inostrannye_okupy.save()
        serializer = InostrannyeOkupySerializer(instance=inostrannye_okupy)
        return Response(serializer.data)

    # delete 
    def delete_inostrannye_okupy(self, request, pk):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        inostrannye_okupy = InostrannyeOkupy.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_inostrannye_okupy(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        serializer = InostrannyeOkupySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    @swagger_auto_schema(operation_summary="getting all of the news form site", request_body=SubReestrSerializer)
    def addSub(cls, request, id : int):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        # serializer = SubReestrSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        SubReestr.objects.create(fk=Reestr.objects.get(pk=id), title=request.data['title']).save();

        return Response({"detail" : "success"})

    
    def addSu2b2(cls, request, id : int):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        # serializer = SubReestrSerializer(data=request.data)
        # if serializer.is_valid():
        #     
        inostrannye_okupy = SubReestr.objects.filter(fk=Reestr.objects.get(pk=id))[0]
        
        serializer = SubReestrSerializer(instance=inostrannye_okupy, many=True)

        return Response(serializer.data)

    def addSu2b3(cls, request, id : int):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                            data={"detail" : "permission denied"})
        # serializer = SubReestrSerializer(data=request.data)
        # if serializer.is_valid():
        #     
        inostrannye_okupy = SubReestr.objects.filter(pk=id)[0].delete()
        return Response({"detail" : "success"})