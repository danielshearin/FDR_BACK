from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from taggit.managers import TaggableManager



CITY_CHOICES = [
    ('asheville', 'Asheville'),
    ('durham', 'Durham'),
    ('atlanta', 'Atlanta'),
    ('nyc', 'NYC')
]


TIME_CHOICES = [
    ('all_times', 'ALL Times'),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('late_night', 'Late Night'),
    ('brunch', 'Brunch'),
    ('breakfast_and_lunch', 'Breakfast and Lunch'),
    ('lunch_dinner', 'Lunch and Dinner'),
    ('breakfast_lunch_dinner', 'Breakfast lunch and dinner'),
    ('dinner_and_late_night', 'Dinner and Late Night'),
    ('lunch_dinner_and_late_night', 'Lunch, Dinner and Late Night'),
]

DAY_CHOICES = [
    ('all_days', 'ALL DAYS'),
    ('weekdays', 'Weekdays'),
    ('weekends', 'Weekends'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
]

DIETARY_CHOICES = [
    ('none', 'none'),
    ('Vegan', 'Vegan'),
    ('Vegetarian', 'Vegetarian'),
    ('Gluten-free', 'Gluten-free'),
    ('Vegetarian and Gluten-free', 'Vegetarian and GF'),
    ('Vegan and Gluten-free', 'Vegan and GF'),
    ('Dairy-free', 'Dairy-free')
]

TAG_CHOICES = [
    ('vegan', 'Vegan'),
    ('vegetarian', 'Vegetarian'),
    ('gluten_free', 'Gluten-Free'),
    ('dairy_free', 'Dairy-free'),
]


class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40, choices=CITY_CHOICES, default='Asheville')
    street = models.CharField(max_length=40)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=14, null=False, blank=False, unique=True)
    website = models.CharField(max_length=60, null=True, blank=True)
    longitude = models.FloatField(max_length=40,null=True, blank=True)
    latitude = models.FloatField(max_length=40,null=True, blank=True)
    coordinates = models.CharField(max_length=40, null=True, blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to="images")
    
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ['restaurant']
    

class MenuItem(models.Model):
    item = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    # location = models.ForeignKey(Restaurant, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    day = models.CharField(max_length=40, null=True, blank=True, choices=DAY_CHOICES, default="ALL DAYS")
    time = models.CharField(max_length=40,choices=TIME_CHOICES, default="ALL TIMES")
    open_time = models.IntegerField()
    close_time = models.IntegerField()
    dietary = models.CharField(max_length=40, null=True, blank=True, choices=DIETARY_CHOICES, default='none')
    tags = TaggableManager(blank=True)
    
    # def publish(self):
    #     self.save()
        
    def __str__(self):
        return self.item
    
    # class Meta:
    #     ordering = ['item']
