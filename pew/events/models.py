from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from django_markdown.models import MarkdownField


class FutureEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(event_dt__gte=timezone.now())\
            .filter(published__exact=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownField()
    event_dt = models.DateTimeField(
        verbose_name="When is the event?")
    location = models.CharField(max_length=200, blank=True)
    published = models.BooleanField(default=False, db_index=True)
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'event-details',
            args=[self.event_dt.year, self.event_dt.month, self.slug])

    class Meta(object):
        ordering = ['event_dt']

    objects = models.Manager()
    upcoming = FutureEventManager()
