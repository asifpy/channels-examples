from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'

    def ready(self):
        from . import handlers
