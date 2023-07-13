from django.contrib import admin
from .models import AddressModel
from socket import gethostbyname
from django import forms
import logging

log = logging.getLogger(__name__)


class AddressAdminForm(forms.ModelForm):
    def clean(self):
        try:
            ip = gethostbyname(self.cleaned_data["url"])
        except Exception as e:
            raise forms.ValidationError(
                f"Unable to create record for {self.cleaned_data['url']}: {e}"
            )
        else:
            self.cleaned_data["ip"] = ip


@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    fields = ["url"]

    form = AddressAdminForm
