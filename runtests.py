#!/usr/bin/env python
import sys

from os.path import dirname, abspath

from django.conf import settings
from django import VERSION as DJANGO_VERSION


middleware = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

if DJANGO_VERSION < (1,3):
    middleware.append('cbv.middleware.DeferredRenderingMiddleware')

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE="sqlite3",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "idios",
            "idios.tests",
        ],
        MIDDLEWARE_CLASSES=middleware,
        AUTH_PROFILE_MODULE="tests.SimpleProfile",
        ROOT_URLCONF="idios.tests.urls"
    )


from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ["tests"]
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
