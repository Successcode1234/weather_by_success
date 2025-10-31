# from django.apps import AppConfig


# class MyappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'

# class LoginsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'logins'

#     def ready(self):
#         import logins.signals

from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals

