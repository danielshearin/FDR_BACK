from rest_framework import serializers
from .models import Restaurant, Todo, MenuItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'city', 'street', 'zip', 'phone', 'longitude', 'latitude', 'coordinates')
        
        

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'item', 'restaurant', 'price', 'description', 'day', 'dietary', 'open_time', 'close_time')
        
        
        
# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ('id', 'title', 'description', 'completed')

