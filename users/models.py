from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.db import models

from event_management import settings

# Create your models here.""""
# class UserProfile(models.Model):
#     user=models.OneToOneField(
#         settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,primary_key=True, related_name='userprofile'
#     )
#     profile_image=models.ImageField(upload_to='profile_image',blank=True)
#     phone=PhoneNumberField(region="BD")
    
#     def __str__(self):
#         return f"{self.user.username } Profile"
    

class CustomUser(AbstractUser):
	profile_image = models.ImageField(upload_to='profile_image',blank=True)
	phone = models.CharField(blank=True) 

	def __str__(self):
		return self.username
