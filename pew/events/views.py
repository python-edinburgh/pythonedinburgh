from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Event


class EventDetails(DetailView):
    model = Event
    context_object_name = 'event'
