from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Event CRUD
    # path('events/create/', views.create_event, name='create_event'),
    path('events/create/', views.Create_Event.as_view(), name='create_event'),
    # path('events/update/<int:id>/', views.update_event, name='update_event'),
    path('events/update/<int:pk>/', views.Update_Event.as_view(), name='update_event'),
    # path('events/delete/<int:id>/', views.delete_event, name='delete_event'),
    path('events/delete/<int:pk>/', views.Delete_event.as_view(), name='delete_event'),
    # path('events/<int:id>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/', views.EVENT_Detail.as_view(), name='event_detail'),
    path('event/<int:id>/remove-participate/<int:user_id>',views.remove_participant,name='remove_participate'),

    # Participant & Category
    path('categories/add/', views.add_category, name='add_category'),
    
    path('event/<int:event_id>/rsvp/',views.rsvp_event,name='rsvp-event'),
    # path('event/participant_dashboard/',views.participant_dashboard,name='rsvp_all')
    path('event/participant_dashboard/',views.ParticipantDashboardView.as_view(),name='rsvp_all')
     
]
