from rest_framework import serializers
from .models import Room
from users.serializers import TinyUserSerializer
# class RoomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=140)
#     price  = serializers.IntegerField()
#     bedrooms = serializers.IntegerField()
#     instant_book = serializers.BooleanField()

class RoomSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer()
    class Meta:
        model = Room
        fields = ("pk", "name", "price", "bedrooms", "instant_book", "user")

class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
