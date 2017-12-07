
from __future__ import absolute_import

import os

from django.conf.urls import url

from . import views
from .settings import oauth2_settings


app_name = "oauth2_provider"


base_urlpatterns = [
    url(r"^authorize/$", views.AuthorizationView.as_view(), name="authorize"),
    url(r"^token/$", views.TokenView.as_view(), name="token"),
    url(r"^revoke_token/$", views.RevokeTokenView.as_view(), name="revoke-token"),
    url(r"^introspect/$", views.IntrospectTokenView.as_view(), name="introspect"),
]


management_urlpatterns = [
    # Application management views
    url(r"^applications/$", views.ApplicationList.as_view(), name="list"),
    url(r"^applications/register/$", views.ApplicationRegistration.as_view(), name="register"),
    url(r"^applications/(?P<pk>[\w-]+)/$", views.ApplicationDetail.as_view(), name="detail"),
    url(r"^applications/(?P<pk>[\w-]+)/delete/$", views.ApplicationDelete.as_view(), name="delete"),
    url(r"^applications/(?P<pk>[\w-]+)/update/$", views.ApplicationUpdate.as_view(), name="update"),
    # Token management views
    url(r"^authorized_tokens/$", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    url(r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$", views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
]


# If server is of `RESOURCE_TYPE`, then have only resource_server_urls.
if oauth2_settings.SERVER_TYPE == 'RESOURCE':
    if not oauth2_settings.CREATE_AUTH_TOKEN_URL:
        print('Setting `CREATE_AUTH_TOKEN_URL` is mandatory for `SERVER_TYPE = Resource`')
        os._exit(1)

    base_urlpatterns = [
        url(r"^resource/token/$", views.ResourceServerTokenAPIView.as_view(), name="resource_server_create_token"),
    ]
    management_urlpatterns = []

urlpatterns = base_urlpatterns + management_urlpatterns
