from django.db import models

from django_markdown.models import MarkdownField


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownField()
    event_dt = models.DateTimeField(
        name="When",
        verbose_name="When is the event?")

    def __str__(self):
        return self.title