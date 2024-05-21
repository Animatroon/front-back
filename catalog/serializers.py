from rest_framework import serializers
from .models import Catalog, Reestr, PoiskPravoobladateley, InostrannyeOkupy, SubReestr

        
class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog 
        fields = ['id', 'name', 'file']

     
     
          
class ReestrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reestr 
        fields = ['id', 'name']

class SubReestrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubReestr 
        fields = ['title']

class PoiskPravoobladateleySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoiskPravoobladateley 
        fields = ['id', 'name', 'performer', 'individ_face', 'repertoire', 'contract_number', 'datу_of_signing']
        

class InostrannyeOkupySerializer(serializers.ModelSerializer):
    class Meta:
        model =  InostrannyeOkupy
        fields = ['id', 'title']
        