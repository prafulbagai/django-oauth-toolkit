
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from django.conf.settings import OAUTH2_PROVIDER

from models import Scopes

app_authorized = Signal(providing_args=["request", "token"])


"""Custom Signal to update scopes in settings file."""


@receiver(post_save, sender=Scopes, dispatch_uid="update_scopes_settings")
def update_scopes(sender, instance, **kwargs):
    scopes = Scopes.objects.all()
    scope_settings = {scope.scope: scope.detail for scope in scopes}
    OAUTH2_PROVIDER.update({'SCOPES': scope_settings})
