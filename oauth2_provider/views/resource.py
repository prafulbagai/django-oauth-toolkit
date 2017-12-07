"""OAuth2 Views.py."""
import requests

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from oauth2_provider.models import AccessToken
from oauth2_provider.settings import oauth2_settings


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
        data = request.data.get
        pdata = {
            'scope': data('scope'),
            'grant_type': data('grant_type')
        }
        auth = (data('client_id'), data('client_secret'))
        r = requests.post(oauth2_settings.CREATE_AUTH_TOKEN_URL, data=pdata,
                          auth=auth)
        try:
            response = r.json()
        except Exception as e:
            response = {
                'error': str(e)
            }
        return Response(response)
