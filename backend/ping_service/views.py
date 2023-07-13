from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from . import serializers
from . import models

# address - returns addresses
# address/pings - returns pings associated with address
# pings - returns list of pings
# recent - returns all latest pings for all addresses

# class AddressView(viewsets.List)

class AddressView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AddressSerializer
    permission_classses = [AllowAny]
    queryset = models.AddressModel.objects.all()

class PingView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.PingSerializer
    permission_classses = [AllowAny]
    queryset = models.PingModel.objects.all()

    # @action(
    #     methods=("get",),
    #     detail=False,
    # )
    # def get_latest(self, request, **kwargs) -> Response:

    #     self.get_queryset().filter()

# @api_view(["GET"])
# def get_recent_view(request):
#     return
