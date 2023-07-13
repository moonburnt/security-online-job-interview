from django.apps import AppConfig

class PingServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ping_service"

    def ready(self):
        from .services import run_ping_fetcher
        print("Running thread service")
        run_ping_fetcher()
