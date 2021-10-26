from rest_framework import serializers
from .models import Restaurant, MenuItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'city', 'street', 'zip', 'phone', 'website', 'longitude', 'latitude', 'coordinates', 'photo')
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(many=False, read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ('id', 'item', 'price', 'description', 'day', 'dietary', 'open_time', 'close_time', 'restaurant')


class ItemSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('low_price', 'high_price', 'time', 'day', 'dietary')