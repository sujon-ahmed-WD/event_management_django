from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.dashboard, name='dashboard'),

    # Event CRUD
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:id>/', views.update_event, name='update_event'),
    path('events/delete/<int:id>/', views.delete_event, name='delete_event'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),

    # Participant & Category
    path('participants/add/', views.add_participant, name='add_participant'),
    path('categories/add/', views.add_category, name='add_category'),
]
