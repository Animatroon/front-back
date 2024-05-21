from rest_framework import serializers
from .models import News, AdditionalPhotosOfNews


class NewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = News 
        # fields = ['id', 'title', 'main_photo', 'text', 'video']
        fields = ['id', 'title', 'main_photo', 'text']


class AdditionalPhotosSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)

    class Meta:
        model = AdditionalPhotosOfNews
        fields = ['fk', 'photo']
        


   