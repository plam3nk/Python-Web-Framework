from django.apps import AppConfig


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_web_tools.web'

    def ready(self):
        import django_web_tools.web.signals
