from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Category, Participant
from .forms import EventForm, ParticipantForm, CategoryForm

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    type= request.GET.get('type')
    print(type)
    today = date.today()
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    context = {
        'events': events,
        'total_events': events.count(),
        'total_participants': Participant.objects.count(),
        'total_categories': Category.objects.count(),
        'upcoming_events': events.filter(date__gt=today).count(),
        'past_events': events.filter(date__lt=today).count(),
        'todays_events': events.filter(date=today),
    }
    return render(request, 'event.html', context)

def create_event(request):
    form = EventForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Event Created Successfully")
        return redirect('dashboard')
    return render(request, 'event_form.html', {'form': form})

def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance=event)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Event Updated Successfully")
        return redirect('dashboard')
    return render(request, 'event_form.html', {'form': form})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('dashboard')
    return render(request, 'delete_event.html', {'event': event})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event_detail.html', {'event': event})

def add_participant(request):
    form = ParticipantForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Participant Added Successfully")
        return redirect('dashboard')
    return render(request, 'participant_form.html', {'form': form})

def add_category(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Category Added Successfully")
        return redirect('dashboard')
    return render(request, 'category_form.html', {'form': form})
