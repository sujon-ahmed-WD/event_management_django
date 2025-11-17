# from datetime import date
# from django.conf import settings
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
# from django.core.mail import send_mail
# from django.views import View
# from django.views.generic import UpdateView, DeleteView, DetailView, TemplateView
# from django.utils.decorators import method_decorator
# from django.urls import reverse_lazy
# from django.db.models import Count

# from .models import Event, Category
# from .forms import EventForm, CategoryForm

# User = get_user_model()

# # ----------------------- User Role Checks -----------------------
# def is_admin(user):
#     return user.is_superuser or user.groups.filter(name='admin').exists()

# def is_organizer(user):
#     return user.is_authenticated and (user.is_superuser or user.groups.filter(name__iexact='Organizer').exists())

# def admin_or_organizer(user):
#     return is_admin(user) or is_organizer(user)

# def is_participant(user):
#     return user.groups.filter(name='participate').exists()

# # ----------------------- Home -----------------------
# def home(request):
#     return render(request, 'home.html')

# # ----------------------- Dashboard -----------------------
# @login_required
# def dashboard(request):
#     today = date.today()
#     events = Event.objects.select_related('category').prefetch_related('participant')
    
#     context = {
#         'events': events,
#         'total_events': events.count(),
#         'total_categories': Category.objects.count(),
#         'upcoming_events': events.filter(date__gt=today).count(),
#         'past_events': events.filter(date__lt=today).count(),
#         'todays_events': events.filter(date=today).count(),
#     }
    
#     return render(request, 'event.html', context)

# # ----------------------- Event Create -----------------------
# @user_passes_test(is_organizer, login_url='no-permission')
# def create_event(request):
#     form = EventForm(request.POST or None, request.FILES or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         messages.success(request, "Event Created Successfully")
#         return redirect('dashboard')
#     return render(request, 'event_form.html', {'form': form})

# @method_decorator(user_passes_test(is_organizer, login_url='no-permission'), name='dispatch')
# class Create_Event(View):
#     template_name = 'event_form.html'

#     def get(self, request, *args, **kwargs):
#         form = EventForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = EventForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Event Created Successfully")
#             return redirect('dashboard')
#         return render(request, self.template_name, {'form': form})

# # ----------------------- Event Update -----------------------
# @user_passes_test(is_organizer, login_url='no-permission')
# def update_event(request, id):
#     event = get_object_or_404(Event, id=id)
#     form = EventForm(request.POST or None, request.FILES or None, instance=event)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         messages.success(request, "Event Updated Successfully")
#         return redirect('dashboard')
#     return render(request, 'event_form.html', {'form': form})

# @method_decorator(user_passes_test(is_organizer, login_url='no-permission'), name='dispatch')
# class Update_Event(UpdateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'event_form.html'
#     success_url = reverse_lazy('dashboard')
#     pk_url_kwarg = 'pk'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['event'] = self.get_object()
#         return context

#     def form_valid(self, form):
#         messages.success(self.request, "Event Updated Successfully")
#         return super().form_valid(form)

# # ----------------------- Event Delete -----------------------
# @user_passes_test(is_organizer, login_url='no-permission')
# def delete_event(request, id):
#     event = get_object_or_404(Event, id=id)
#     if request.method == 'POST':
#         event.delete()
#         messages.success(request, "Event Deleted Successfully")
#         return redirect('dashboard')
#     return render(request, 'event_form.html', {'event': event})

# @method_decorator(user_passes_test(is_organizer, login_url='no-permission'), name='dispatch')
# class Delete_event(DeleteView):
#     model = Event
#     template_name = 'event_form.html'
#     success_url = reverse_lazy('dashboard')
#     pk_url_kwarg = 'pk'

#     def delete(self, request, *args, **kwargs):
#         messages.success(request, "Event Deleted Successfully")
#         return super().delete(request, *args, **kwargs)

# # ----------------------- Remove Participant -----------------------
# @user_passes_test(is_admin, login_url='no-permission')
# def remove_participant(request, event_id, user_id):
#     event = get_object_or_404(Event, id=event_id)
#     user = get_object_or_404(User, id=user_id)
#     if request.method == "POST":
#         event.participant.remove(user)
#         messages.success(request, f"{user.username} has been removed from the event.")
#         return redirect('event_detail', id=event.id)
#     return render(request, 'rmb_participate.html', {'event': event, 'user': user})

# # ----------------------- Event Detail -----------------------
# def event_detail(request, id):
#     event = get_object_or_404(Event, id=id)
#     return render(request, 'event_detail.html', {'event': event})

# class EVENT_Detail(DetailView):
#     model = Event
#     template_name = 'event_detail.html'
#     pk_url_kwarg = 'pk'

# # ----------------------- Category -----------------------
# @user_passes_test(is_organizer, login_url='no-permission')
# def add_category(request):
#     form = CategoryForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         messages.success(request, "Category Added Successfully")
#         return redirect('dashboard')
#     return render(request, 'category_form.html', {'form': form})

# # ----------------------- RSVP -----------------------
# @login_required
# def rsvp_event(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     user = request.user

#     if event.participant.filter(id=user.id).exists():
#         messages.warning(request, "You have already RSVP'd to this event.")
#     else:
#         event.participant.add(user)
#         messages.success(request, "RSVP successful! A confirmation email has been sent.")

#         send_mail(
#             subject="RSVP Confirmation Email",
#             message=f"Aslamolikum {user.username},\n\nYou have successfully RSVP'd to the event {event.name}.",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[user.email],
#             fail_silently=True
#         )

#     return redirect('event_detail', id=event.id)

# # ----------------------- Participant Dashboard -----------------------
# @login_required
# def participant_dashboard(request):
#     rsvp_events = request.user.rsvp_events.all()
#     return render(request, 'participant_dashboard.html', {"rsvp_events": rsvp_events})

# class ParticipantDashboardView(TemplateView):
#     template_name = 'participant_dashboard.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rsvp_events'] = self.request.user.rsvp_events.all()
#         return context
#---------------------------------------------------------###----------------------------------------------------------------------------------
from datetime import date
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, TemplateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Count

from .models import Event, Category
from .forms import EventForm, CategoryForm

User = get_user_model()

# -----------------------------------------------------------
# 🔐 Role Check Helpers (Optimized)
# -----------------------------------------------------------
def is_admin(user):
    return user.is_superuser or user.groups.filter(name='admin').exists()

def is_organizer(user):
    return user.is_authenticated and (
        user.is_superuser or user.groups.filter(name__iexact='organizer').exists()
    )

def is_participant(user):
    return user.groups.filter(name='participate').exists()


# -----------------------------------------------------------
# 🏠 Home
# -----------------------------------------------------------
def home(request):
    return render(request, 'home.html')


# -----------------------------------------------------------
# 📊 Dashboard (Optimized Query)
# -----------------------------------------------------------
@login_required
def dashboard(request):
    today = date.today()

    events = Event.objects.select_related('category').prefetch_related('participant')

    context = {
        'events': events,
        'total_events': events.count(),
        'total_categories': Category.objects.count(),
        'upcoming_events': events.filter(date__gt=today).count(),
        'past_events': events.filter(date__lt=today).count(),
        'todays_events': events.filter(date=today).count(),
    }
    return render(request, 'event.html', context)


# -----------------------------------------------------------
# 📌 Event Create
# -----------------------------------------------------------
@user_passes_test(is_organizer, login_url='no-permission')
def Create_Event(request):
    form = EventForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Event Created Successfully")
        return redirect('dashboard')

    return render(request, 'event_form.html', {'form': form})


@method_decorator(user_passes_test(is_organizer, login_url='no-permission'), name='dispatch')
class CreateEventView(View):
    template_name = 'event_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': EventForm()})

    def post(self, request):
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Created Successfully")
            return redirect('dashboard')

        return render(request, self.template_name, {'form': form})


# -----------------------------------------------------------
# ✏ Event Update
# -----------------------------------------------------------
@user_passes_test(is_organizer, login_url='no-permission')
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Event Updated Successfully")
        return redirect('dashboard')

    return render(request, 'event_form.html', {'form': form})


@method_decorator(user_passes_test(is_organizer, login_url='no-permission'), name='dispatch')
class UpdateEventView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        messages.success(self.request, "Event Updated Successfully")
        return super().form_valid(form)


# -----------------------------------------------------------
# 🗑 Event Delete
# -----------------------------------------------------------
@user_passes_test(is_organizer, login_url='no-permission')
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('dashboard')

    return render(request, 'event_form.html', {'event': event})


@method_decorator(user_passes_test(is_organizer, login_url='no-permission'), name='dispatch')
class DeleteEventView(DeleteView):
    model = Event
    template_name = 'event_form.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Event Deleted Successfully")
        return super().delete(request, *args, **kwargs)


# -----------------------------------------------------------
# ❌ Remove Participant
# -----------------------------------------------------------
@user_passes_test(is_admin, login_url='no-permission')
def remove_participant(request, event_id, user_id):
    event = get_object_or_404(Event, id=event_id)
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        event.participant.remove(user)
        messages.success(request, f"{user.username} removed from event.")
        return redirect('event_detail', id=event.id)

    return render(request, 'rmb_participate.html', {'event': event, 'user': user})


# -----------------------------------------------------------
# 🔎 Event Detail
# -----------------------------------------------------------
def event_detail(request, id):
    return render(request, 'event_detail.html', {
        'event': get_object_or_404(Event, id=id)
    })


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    pk_url_kwarg = 'pk'


# -----------------------------------------------------------
# 📂 Category Add
# -----------------------------------------------------------
@user_passes_test(is_organizer, login_url='no-permission')
def add_category(request):
    form = CategoryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Category Added Successfully")
        return redirect('dashboard')

    return render(request, 'category_form.html', {'form': form})


# -----------------------------------------------------------
# 🎟 RSVP Event
# -----------------------------------------------------------
@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    if event.participant.filter(id=user.id).exists():
        messages.warning(request, "Already RSVP'd.")
    else:
        event.participant.add(user)
        messages.success(request, "RSVP successful!")

        send_mail(
            subject="RSVP Confirmation",
            message=f"Aslamolikum {user.username},\nYou have RSVP'd for {event.name}.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True
        )

    return redirect('event_detail', id=event.id)


# -----------------------------------------------------------
# 🧍 Participant Dashboard
# -----------------------------------------------------------
@login_required
def participant_dashboard(request):
    return render(request, 'participant_dashboard.html', {
        "rsvp_events": request.user.rsvp_events.all()
    })


class ParticipantDashboardView(TemplateView):
    template_name = 'participant_dashboard.html'

    def get_context_data(self, **kwargs):
        return {
            'rsvp_events': self.request.user.rsvp_events.all()
        }
