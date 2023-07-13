from rest_framework import serializers
from ping_service.models import PingModel, AddressModel
import logging

log = logging.getLogger(__name__)

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = "__all__"

class AddressUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ("url",)

class PingSerializer(serializers.ModelSerializer):
    address = AddressUrlSerializer()

    class Meta:
        model = PingModel
        exclude = ("id",)


