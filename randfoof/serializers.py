from rest_framework import serializers

from randfoof.models import *



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

class RestaurentSerializer(serializers.ModelSerializer):
    # dishes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Restaurent
        fields = ["id", "name", "latitude", "longitude", "picture", "dishes"]
        depth = 1

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"