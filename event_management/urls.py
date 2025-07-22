from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls



urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('event.urls')),
    path('user/',include("users.urls")),
    path('core/', include("core.urls"))
    
    
]+ debug_toolbar_urls()
