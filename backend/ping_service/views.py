from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers
from . import models

class AddressView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AddressSerializer
    permission_classses = [AllowAny]
    queryset = models.AddressModel.objects.all()

    @action(
        methods=("get",),
        detail=True
    )
    def pings(self, request, **kwargs) -> Response:
        queryset = models.PingModel.objects.filter(address=self.get_object()).order_by("created")
        serialized = serializers.PingSerializerMinimal(queryset, many=True)

        return Response(
            serialized.data,
            status = status.HTTP_200_OK,
        )

class PingView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.PingSerializer
    permission_classses = [AllowAny]
    queryset = models.PingModel.objects.all()

    @action(
        methods=("get",),
        detail=False,
    )
    def latest(self, request, **kwargs) -> Response:
        """Get latest pings to all addresses"""

        # TODO: rework into queryset magic
        ret = []

        for i in models.AddressModel.objects.all():
            ret.append(self.get_serializer(i.pings.order_by("created").last()).data)

        return Response(
            data = ret,
            status = status.HTTP_200_OK,
        )


def get_chart(request):
    return render(request, f'index.html')
