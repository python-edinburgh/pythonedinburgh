from django.views.generic import DetailView

from .models import Event


class EventDetails(DetailView):
    model = Event
    context_object_name = 'event'
