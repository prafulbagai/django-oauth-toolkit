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
    packages=['oauth2_provider'],
    author='Praful Bagai',
    url='https://bitbucket.org/pseynse/oauth2',
    description=DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
)
