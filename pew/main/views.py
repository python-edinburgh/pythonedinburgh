from django.shortcuts import render

from events.models import Event


def home(request):
    return render(
        request,
        'pew/home.html',
        {
            'upcoming_events': Event.upcoming.all()
        })
