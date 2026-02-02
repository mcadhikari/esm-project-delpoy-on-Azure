"""
WSGI config for esm_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# 
import os
from django.core.wsgi import get_wsgi_application

if os.getenv("DJANGO_ENVIRONMENT") == "azure":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "esm_project.deployment"
    )
else:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "esm_project.settings"
    )

application = get_wsgi_application()
