from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer, MenuItemSerializer, ItemSearchSerializer
from .models import Restaurant, MenuItem
from rest_framework.generics import CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.

class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
class MenuItemView(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    
class SearchItemsView(APIView):
    parser_classes = [JSONParser]
    
    def post(self, request, format=None):
        price_low = request.data['price_low']
        price_high = request.data['price_high']
        time = request.data['time'] 
        day = request.data['day']
        dietary = request.data['dietary']
        
        menu_items = MenuItem.objects.filter(price__gte=price_low, price__lte=price_high, open_time__lte=time, close_time__gte=time)

        serializer = MenuItemSerializer(menu_items, many=True)
        
        return Response(serializer.data)
        # return Response(day)
