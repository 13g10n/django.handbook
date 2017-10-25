from django.apps import AppConfig


class ManualsConfig(AppConfig):
    name = 'manuals'

    def ready(self):
        import badges.signals
