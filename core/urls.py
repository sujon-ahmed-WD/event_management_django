from django.urls import path
from core.views import hom,no_permission
urlpatterns=[
    
    path('',hom,name="home"),
    path('no_permission/',no_permission,name='no-permission'),
    # path('dashboard/', dashboard_redirect, name='dashboard')
    
]