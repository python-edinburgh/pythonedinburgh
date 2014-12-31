from django.shortcuts import render

from events.models import Event


def home(request):
    return render(
        request,
        'pew/home.html',
        _home_context_dict()
        )


def _home_context_dict():
    return {
        'upcoming_events': Event.upcoming.all()
    }
