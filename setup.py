"""Setup modeule."""
from setuptools import setup

DESCRIPTION = 'OAuth2 Provider for Django'
VERSION = '1.0.0'

INSTALL_REQUIRES = [
    'django >= 1.11',
    'oauthlib >= 2.0.3',
    'requests >= 2.13.0',
    'djangorestframework >= 3.7.1',
]

setup(
    name='django-oauth-toolkit',
    version=VERSION,
    packages=['oauth2_provider', 'oauth2_provider.contrib', 'oauth2_provider.contrib.rest_framework',
              'oauth2_provider.management', 'oauth2_provider.views', 'oauth2_provider.templates',
              'oauth2_provider.migrations'],
    include_package_data=True,
    zip_safe=False,
    author='Praful Bagai',
    url='https://github.com/prafulbagai/django-oauth-toolkit',
    description=DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
)
