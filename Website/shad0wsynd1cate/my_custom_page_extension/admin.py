from django.contrib import admin

# Register your models here.

# Page extension imports:
from cms.extensions import PageExtensionAdmin

# Import our model from ``models.py``:
from .models import PageFieldExtension

class PageFieldExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(PageFieldExtension, PageFieldExtensionAdmin)
