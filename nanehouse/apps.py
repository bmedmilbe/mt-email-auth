from django.apps import AppConfig


class NanehouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nanehouse'


    def ready(self) -> None:
        import nanehouse.signals.hendlers
