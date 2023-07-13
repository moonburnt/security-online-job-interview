from rest_framework import serializers
from ping_service.models import PingModel, AddressModel
import logging

log = logging.getLogger(__name__)

class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingModel
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = "__all__"
