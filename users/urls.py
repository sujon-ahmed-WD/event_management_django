
from django.urls import path
from users.views import sign_up,sign_in,logout_view

urlpatterns = [
    path('register/',sign_up, name='sign_up'),
    path('sign-in/',sign_in,name="sign_in"),
    path('logout/', logout_view, name='logout'),
    
    
]