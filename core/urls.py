from django.urls import path
from core.views import hom
urlpatterns=[
    
    path('home/',hom,name="home")
]