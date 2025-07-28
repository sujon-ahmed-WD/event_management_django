from django.urls import path
from core.views import hom,no_permission
urlpatterns=[
    
    path('home/',hom,name="home"),
    path('no_permission/',no_permission,name='no-permission')
    
]