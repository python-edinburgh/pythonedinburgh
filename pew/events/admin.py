from django.contrib import admin

from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget

from . import models


class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownField: {'widget': AdminMarkdownWidget}}


admin.site.register(models.Event)