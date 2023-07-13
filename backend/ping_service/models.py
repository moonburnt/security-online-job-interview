from django.db import models


class PingModel(models.Model):
    value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ping to {self.pinged_address} on {self.created}: {self.value}"


class AddressModel(models.Model):
    url = models.URLField(
        unique=True,
    )
    pings = models.ForeignKey(
        to=PingModel,
        related_name="pinged_address",
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.url
