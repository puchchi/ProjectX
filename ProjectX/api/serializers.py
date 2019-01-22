from rest_framework_mongoengine import serializers

from models import Place

class PlaceSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Place
        fields = '__all__'
