from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer, MenuItemSerializer, ItemSearchSerializer
from .models import Restaurant, MenuItem
from rest_framework.generics import CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db.models import Q

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
        def diet():
            dietary = request.data['dietary']
            # print(dietary)
            if dietary == []:
                dietary = ['none']
                print('null success')
            elif dietary == ['none']:
                dietary = ['none']
                print('none success')
            elif dietary.count('vegetarian') == 1 and dietary.count('gluten_free') == 1:
                dietary = ['vegetarian_and_gf', 'vegan_and_gf']
                print('veggie gf success')
            elif dietary.count('vegan') == 1 and dietary.count('gluten_free') == 1:
                dietary = ['vegan_and_gf']
                print('vegan gf success')
            else:
                return dietary
            # print(dietary)
            return dietary
        
        def day_list():
            day = []
            day_formdata = request.data['day']
            if day_formdata == [] or day.count('none') == 1:
                print('day is null')
                day.extend(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'weekends', 'weekdays', 'all_days'])
            if day_formdata.count('weekdays') == 1:
                day.extend(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'weekdays'])
            if day_formdata.count('weekends') == 1:
                day.extend(['saturday', 'sunday', 'weekends'])
            if day_formdata.count('sunday') == 1:
                day.extend(['saturday', 'weekends'])
            if day_formdata.count('saturday') == 1:
                day.extend(['sunday', 'weekends'])
            if day_formdata.count('monday') == 1:
                day.extend(['monday', 'weekdays'])
            if day_formdata.count('tuesday') == 1:
                day.extend(['tuesday', 'weekdays'])
            if day_formdata.count('wednesday') == 1:
                day.extend(['wednesday', 'weekdays'])
            if day_formdata.count('thursday') == 1:
                day.extend(['thursday', 'weekdays'])
            if day_formdata.count('friday') == 1:
                day.extend(['friday', 'weekdays'])
            else:
                day.extend(day)
            return day
        
        price_low = request.data['price_low']
        price_high = request.data['price_high']
        time = request.data['time'] 
        
        menu_items = MenuItem.objects.filter((Q(day__in=day_list()) | Q(tags__name__in=day_list()) | Q(day="all_days")) & Q(price__gte=price_low) & Q(price__lte=price_high) & Q(open_time__lte=time) & Q(close_time__gte=time) & Q(tags__name__in=diet()))

        serializer = MenuItemSerializer(menu_items, many=True)
        
        return Response(serializer.data)
        # return Response(day)
