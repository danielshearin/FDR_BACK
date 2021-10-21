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
                dietary = ['vegetarian_and_gf']
                print('veggie gf success')
            elif dietary.count('vegan') == 1 and dietary.count('gluten_free') == 1:
                dietary = ['vegan_and_gf']
                print('vegan gf success')
            else:
                return dietary
            # print(dietary)
            return dietary
        
        def day_list():
            day = request.data['day']
            print(day)
            if day == [] or day == ['none']:
                day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'weekends', 'weekdays', 'all_days']
            else:
                day = day
            print('dayList run')
            print(day)
            return day
        
        price_low = request.data['price_low']
        price_high = request.data['price_high']
        time = request.data['time'] 
        # if day == 'weekends':
        #     return ['weekends', 'saturday', 'sunday']
        # if day == 'weekdays':
        #     return ['weekdays', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        # if day == 'none':
        #     return ['monday', 'tuesday', 'wednesday', 'thursday', 
        #             'friday', 'saturday', 'weekends', 'weekdays', 'all_days']
        
        



        # if dietary == 'none':
        #     return ['none', 'vegetarian', 'vegan', 'gluten_free', 'vegetarian_and_gf', 'vegan_and_gf']
        # if dietary == 'vegetarian':
        #     return ['vegetarian', 'vegan', 'vegetarian_and_gf', 'vegan_and_gf']
        # if dietary == 'vegan':
        #     return ['vegan', 'vegan_and_gf']
        # if dietary == 'gluten_free':
        #     return ['gluten_free', 'vegetarian_and_gf', 'vegan_and_gf']
        
        # menu_items = MenuItem.objects.filter((Q(day__in=day) | Q(day="all_days")) & Q(price__gte=price_low) & Q(price__lte=price_high) & Q(open_time__lte=time) & Q(close_time__gte=time) & Q(tags__name__in=dietary))
        
        menu_items = MenuItem.objects.filter((Q(day__in=day_list()) | Q(tags__name__in=day_list()) | Q(day="all_days")) & Q(price__gte=price_low) & Q(price__lte=price_high) & Q(open_time__lte=time) & Q(close_time__gte=time) & Q(tags__name__in=diet()))

        serializer = MenuItemSerializer(menu_items, many=True)
        
        return Response(serializer.data)
        # return Response(day)
