from django.core.urlresolvers import reverse
from django.db import models

from django_markdown.models import MarkdownField


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownField()
    event_dt = models.DateTimeField(
        verbose_name="When is the event?")
    published = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-details', args=[self.slug])

    class Meta(object):
        ordering = ['event_dt']
