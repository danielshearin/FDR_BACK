from django.contrib import admin
from .models import Todo, MenuItem, Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'zip', 'phone', 'longitude', 'latitude', 'coordinates',)
    
    
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'restaurant', 'price', 'description', 'day', 'open_time', 'close_time')


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(MenuItem, MenuItemAdmin)

admin.site.register(Todo, TodoAdmin)