from django.apps import AppConfig


class CmzConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cmz'

    def ready(self) -> None:
        import cmz.signals.hendlers
    
