from django.contrib import admin
from .models import AddressModel

import logging

log = logging.getLogger(__name__)

@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    fields = ["url"]
