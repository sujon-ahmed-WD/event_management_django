from django.db import models
from django.contrib.auth.models import User

from event_management import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    participant=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='rsvp_events')
    image=models.ImageField(upload_to='event_asset',blank=True,null=True,default='event_asset/default_image.jpg')
    

    def __str__(self):
        return self.name

# class Participant(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     events = models.ManyToManyField(Event, related_name='participants')

#     def __str__(self):
#         return self.name
