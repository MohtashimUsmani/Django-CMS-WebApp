from django.apps import AppConfig


class CustomerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_app'

    def ready(self):
        import customer_app.signals
