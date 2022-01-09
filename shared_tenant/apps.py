from django.apps import AppConfig


class SharedTenantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared_tenant'
