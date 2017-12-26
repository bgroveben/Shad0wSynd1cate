from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin

# Create your models here.

@python_2_unicode_compatible
class Social(CMSPlugin):
    label = models.CahrField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label
