from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    name = models.CharField(
        max_length = 20,
        null = True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('name')
    ]