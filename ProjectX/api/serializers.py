from rest_framework_mongoengine import serializers

from models import Place2
from api.models import URLInput

class PlaceSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Place2
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data["place_name"]
        instance.state = validated_data["state"]
        instance.country = validated_data["country"]
        instance.description = validated_data["description"]
        instance.address = validated_data["address"]
        instance.latitude = float(validated_data["latitude"])
        instance.longitude = float(validated_data["longitude"])
        instance.map_id = validated_data["map_url"]
        instance.place_id = validated_data["place_id"]
        photo_urls = []
        for key in validated_data.keys():
            if (key.find("place_photo_url")!=-1):
                url = URLInput(validated_data[key])
                photo_urls.append(url)
        instance.photo_urls = photo_urls

        instance.save()
        return instance