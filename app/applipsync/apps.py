from django.apps import AppConfig


class ApplipsyncConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applipsync"

    def ready(self):
        import applipsync.signals
