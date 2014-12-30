from django.shortcuts import render

from events.models import Event

def home(request):
    return render(
        request,
        'pew/home.html',
        {
            'events': Event.upcoming.all()
        })
