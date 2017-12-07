
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save

from .models import get_scopes_model
from .settings import oauth2_settings

app_authorized = Signal(providing_args=["request", "token"])


"""Custom Signal to update scopes in settings file."""

Scopes = get_scopes_model()


@receiver(post_save, sender=Scopes, dispatch_uid="update_scopes_settings")
def update_scopes(sender, instance, **kwargs):
    scopes = Scopes.objects.all()
    scope_settings = {scope.scope: scope.detail for scope in scopes}
    oauth2_settings.SCOPES.update(scope_settings)
