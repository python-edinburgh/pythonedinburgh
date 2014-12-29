from __future__ import print_function, absolute_import

from datetime import date, datetime, timedelta
import logging


import yaml
import pytz
import requests
from icalendar import Calendar

import settings


class Event(object):

    def __init__(self, start, title, where, description):
        self.start = start
        self.title = title
        self.where = where
        self.description, self.metadata = self._event_metadata(description)

    def _event_metadata(self, description):

        split_on = "----------"

        if split_on in description:
            description, metadata = description.split(split_on)
            metadata = yaml.load(metadata)
        else:
            metadata = {}

        if 'type' not in metadata:
            metadata['type'] = self.title.split(' ', 1)[0].lower()

        return description, metadata

    def days_until(self):
        until_event = self.start - _now()
        return until_event.days

    def date_string(self):
        if self.start is None:
            return
        date_s = self.start.strftime("%A %d%%s of %B")
        date_s = date_s % _nth(self.start.day)
        return date_s

    def time_string(self):
        if self.start is None:
            return
        time_s = "%d:%02d" % (self.start.hour % 12, self.start.minute)
        ampm = self.start.strftime("%p").lower()
        return time_s + ampm

    @classmethod
    def from_vevent(cls, vevent):

        return Event(
            start=vevent.get('dtstart').dt,
            title=vevent.get('summary').title(),
            where=vevent.get('location').title(),
            description=str(vevent.get('description'))
        )


def _load_calendar():
    logging.debug("Loading Calendar from: %r", settings.ICAL_URL)
    ical_request = requests.get(settings.ICAL_URL)
    cal = Calendar.from_ical(ical_request.text)
    for k in cal.subcomponents:
        logging.debug('Calendar - %r', k)
    return cal


def _now():
    return datetime.now(tz=pytz.utc)


def _nth(num):
    """ Returns the 'th' suffix to the given num. What's that thing called?
    """
    sn = str(num)
    ld = sn[-1]
    if len(sn) == 1 or sn[-2] != '1':
        if ld == '1':
            return 'st'
        elif ld == '2':
            return 'nd'
        elif ld == '3':
            return 'rd'
    return 'th'


def upcoming_events(days=60, cal=None):

    if cal is None:
        cal = _load_calendar()

    now = _now()
    future = now + timedelta(days=days)
    events = []

    for vevent in cal.walk('vevent'):

        start = vevent.get('dtstart').dt

        if isinstance(start, date):
            start = datetime.combine(start, datetime.min.time())

        start = start.replace(tzinfo=pytz.utc)

        if start < now:
            continue

        if start > future:
            continue

        events.insert(0, Event.from_vevent(vevent))

    return events


class NoEvents(Exception):
    pass


def days_until_next_event():

    events = upcoming_events()

    if len(events) == 0:
        raise NoEvents("No events planned")

    event = events[0]
    return event.days_until(), event
