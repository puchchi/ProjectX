from rest_framework_mongoengine import serializers

from models import Place2

class PlaceSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Place2
        fields = '__all__'
