from rest_framework import serializers
from .models import Document


        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document 
        fields = ['id', 'label', 'title', 'file', 'type']
        # fields = ['id', 'label']

   