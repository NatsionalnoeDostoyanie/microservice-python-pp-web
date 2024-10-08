# Общие настройки, которые используются во всех средах (разработка, тестирование, продакшн)

import os
from dotenv import load_dotenv

load_dotenv()

ROOT_URLCONF = "main.urls"

INTERNAL_IPS = [
    "127.0.0.1",
]

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

CSRF_TRUSTED_ORIGINS = [os.getenv("MAIN_URL", "http://")]
CSRF_COOKIE_DOMAIN = os.getenv("CSRF_COOKIE_DOMAIN", ".subdomain.com")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

TRACKING_ACTIVITY = None

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Token YOUR_TOKEN": {"type": "apikey", "in": "header"},
    },
    "USE_SESSION_AUTH": False,
    "JSON_EDITOR": True,
}

DJANGO_SWAGGER = None
