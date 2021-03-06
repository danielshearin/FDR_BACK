from django.contrib import admin
from .models import MenuItem, Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'zip', 'phone', 'website', 'longitude', 'latitude', 'coordinates', 'photo')
    
    
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'restaurant', 'price', 'description', 'day', 'dietary', 'open_time', 'close_time', 'tags')


# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(MenuItem, MenuItemAdmin)
