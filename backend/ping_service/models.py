from django.db import models
import logging

log = logging.getLogger(__name__)


# Validation is done in django admin
class AddressModel(models.Model):
    url = models.CharField(
        unique=True,
        max_length=80,
    )

    ip = models.CharField(
        editable=False,
        max_length=46,
    )

    def __str__(self):
        return self.url

class PingModel(models.Model):
    value = models.FloatField()
    address = models.ForeignKey(
        to=AddressModel,
        related_name="pings",
        null=False,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ping to {self.pinged_address} on {self.created}: {self.value}"
