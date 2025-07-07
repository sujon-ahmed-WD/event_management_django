from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    
    path('', include('event.urls')),
    
]+ debug_toolbar_urls()
