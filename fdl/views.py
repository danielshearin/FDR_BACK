from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer, TodoSerializer, MenuItemSerializer
from .models import Todo, Restaurant, MenuItem

# Create your views here.

class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
class MenuItemView(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

# Create your views here.
# class TodoView(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()