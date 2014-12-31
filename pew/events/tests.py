import datetime
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone


from .models import Event


class EventTestCase(TestCase):
    def test_past_events_dont_show(self):
        evt = Event.objects.create(
            title='Old Event',
            description='this event is over.',
            event_dt=timezone.now() - timedelta(seconds=1),
            location='The Pub',
            published=True,
            slug='old-event',
        )

        self.assertEqual(len(Event.upcoming.all()), 0)

    def test_published_future_events_do_show(self):
        evt = Event.objects.create(
            title='Future Event',
            description='this event is going to be great.',
            event_dt=timezone.now() + timedelta(seconds=5),
            location='The Pub',
            published=True,
            slug='new-event',
        )

        self.assertEqual(Event.upcoming.all()[0], evt)

    def test_unpublished_future_events_dont_show(self):
        evt = Event.objects.create(
            title='Future Event',
            description='this event is going to be great.',
            event_dt=timezone.now() + timedelta(seconds=5),
            location='The Pub',
            published=False,
            slug='new-event',
        )

        self.assertEqual(len(Event.upcoming.all()), 0)

    def test_get_absolute_url(self):
        evt = Event.objects.create(
            title='Future Event',
            description='this event is going to be great.',
            event_dt=timezone.datetime(2015, 3, 12),
            location='The Pub',
            published=False,
            slug='new-event',
        )
        self.assertEqual('/events/2015/3/new-event', evt.get_absolute_url())
