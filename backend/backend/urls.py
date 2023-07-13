from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from ping_service.views import PingView, AddressView, get_chart
import logging

log = logging.getLogger(__name__)

router = DefaultRouter()
router.register("address", AddressView)
router.register("ping", PingView)

from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls")),
    path("chart/",get_chart),
]
