"""OAuth2 Views.py."""
import requests

from django.conf import settings
from rest_framework import serializers
from oauth2_provider.models import AccessToken
from rest_framework.generics import CreateAPIView


class AuthTokenSerializer(serializers.ModelSerializer):
    """Auth Token Serializer."""

    grant_type = serializers.CharField()
    scope = serializers.CharField()
    client_id = serializers.CharField()
    client_secret = serializers.CharField()

    class Meta:
        """AuthTokenSerializer Meta."""

        model = AccessToken
        fields = ('grant_type', 'scope', 'client_id', 'client_secret')


class ResourceServerTokenAPIView(CreateAPIView):
    """
    GET `access_token`.

    Required Parameters. \n
    - `grant_type` :- Set as `client_credentials`.\n
    - `scope` :- Different API accessibility scopes. Separate multiple scopes
    by a whitespace ' '. Current scopes are `user`, `loan`\n
    - `client_id`: Your `client_id`.\n
    - `client_secret`: Your `client_secret`.
    """

    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):

        if not settings.CREATE_AUTH_TOKEN_ENDPOINT:
            return

        data = request.data.get
        pdata = {
            'scope': data('scope'),
            'grant_type': data('grant_type')
        }
        auth = (data('client_id'), data('client_secret'))
        r = requests.post(settings.CREATE_AUTH_TOKEN_URL, data=pdata,
                          auth=auth)
        try:
            r = r.json()
            return
        except Exception as e:
            return
