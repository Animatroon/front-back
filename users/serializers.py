from rest_framework import serializers


from .models import User, Request


# class SH(serializers.ModelSerializer):
#     class Meta:
#         model = SOMEMODEL
#         fields = '__all__'
        # fields = ['id', 'product', 'shop', 'price', 'quantity']



# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Test 
#         fields = '__all__'
        
        

# class TestSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Test2 
#         fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        # fields = ['id', 'username', 'password', 'email', 'user_type']
        fields = "__all__"
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class LogOutSerializer(serializers.Serializer):
    pass

class AllUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"
 
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255)
    

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['email', 'category', 'subject', 'description', 'created_at']