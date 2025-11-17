from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    # Event CRUD
    path('events/create/', views.CreateEventView.as_view(), name='create_event'),
    path('events/update/<int:pk>/', views.UpdateEventView.as_view(), name='update_event'),
    path('events/delete/<int:pk>/', views.DeleteEventView.as_view(), name='delete_event'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),

    # Remove participant
    path('event/<int:event_id>/remove-participate/<int:user_id>', 
         views.remove_participant, 
         name='remove_participate'),

    # Category
    path('categories/add/', views.add_category, name='add_category'),

    # RSVP
    path('event/<int:event_id>/rsvp/', views.rsvp_event, name='rsvp-event'),

    # Participant Dashboard
    path('event/participant_dashboard/', 
         views.ParticipantDashboardView.as_view(), 
         name='rsvp_all'),
]
