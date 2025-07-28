from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Category
from .forms import EventForm, CategoryForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_Organizer(user):
    return user.groups.filter(name='Organizer').exists()

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    today = date.today()
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    events =Event.objects.prefetch_related('participant')
    context = {
        'events': events,
        'total_events': events.count(),
        # 'total_participants': Participant.objects.count(),
        'total_categories': Category.objects.count(),
        'upcoming_events': events.filter(date__gt=today).count(),
        'past_events': events.filter(date__lt=today).count(),
        'todays_events': events.filter(date=today),
    }
    return render(request, 'event.html', context)
@user_passes_test(is_Organizer,login_url='no-permission')
def create_event(request):
    form = EventForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Event Created Successfully")
        return redirect('dashboard')
    return render(request, 'event_form.html', {'form': form})

@user_passes_test(is_Organizer,login_url='no-permission')
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance=event)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Event Updated Successfully")
        return redirect('dashboard')
    return render(request, 'event_form.html', {'form': form})

@user_passes_test(is_Organizer,login_url='no-permission')
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('dashboard')
    return render(request, 'event_form.html', {'event': event})

@user_passes_test(is_admin,login_url='no-permission')
def remove_participate(request,event_id,user_id):
    event=get_object_or_404(Event,id=event_id)
    user=get_object_or_404(User,id=user_id)
    
    if request.method=="POST":
        event.participant.remove(user)
        
        messages.success(request,f"{user.username} hes been removed from the event .. ")
        return redirect('event_detail.html',id=event.id)
    return render(request,'rmb_participate.html',{'event':event,'user':user})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event_detail.html', {'event': event})

@user_passes_test(is_Organizer,login_url='no-permission')
def add_category(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Category Added Successfully")
        return redirect('dashboard')
    return render(request, 'category_form.html', {'form': form})

@login_required
def rsvp_event(request,event_id):
    event=get_object_or_404(Event,id=event_id)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",request.user)
    if request.user in event.participant.all(): # amier aga confromassion jonno 
        messages.warning(request,"you have already RSVP'd to this event. ")
        
    else:
        event.participant.add(request.user)
        messages.success(request,"RSVP Success fully!")
    return redirect('event_detail.html',event_id=event.id)
        