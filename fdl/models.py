from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.utils import timezone



CITY_CHOICES = [
    ('asheville', 'Asheville'),
    ('durham', 'Durham'),
    ('atlanta', 'Atlanta'),
]


TIME_CHOICES = [
    ('all', 'ALL'),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('late night', 'Late Night'),
    ('breakfast and lunch', 'Breakfast and Lunch'),
    ('lunch and dinner', 'Lunch and Dinner'),
    ('dinner and late night', 'Dinner and Late Night'),
    
]

DAY_CHOICES = [
    ('all', 'ALL'),
    ('weekdays', 'Weekdays'),
    ('weekends', 'Weekends'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
    ('frisatsun', 'Fri/Sat/Sun'),
]


class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40, choices=CITY_CHOICES, default='Asheville')
    street = models.CharField(max_length=40)
    zip = models.IntegerField()
    phone = models.IntegerField(null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ['restaurant']
    

class MenuItem(models.Model):
    item = models.CharField(max_length=40)
    restaurant = models.ForeignKey(Restaurant, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    # location = models.ForeignKey(Restaurant, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    day = models.CharField(max_length=40, choices=DAY_CHOICES, default="ALL")
    
    # def publish(self):
    #     self.save()
        
    def __str__(self):
        return self.item
    
    # class Meta:
    #     ordering = ['item']
    

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
    
    