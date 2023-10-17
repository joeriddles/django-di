"""See https://adamj.eu/tech/2019/04/03/django-versus-flask-with-single-file-applications/"""
import html
import sys
from typing import Protocol

from django_di import view
from django_di.context import DI

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from django.utils.crypto import get_random_string

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],    # Disable host header validation
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY=get_random_string(50),
)


# Example service interface
class Reverser(Protocol):
    def reverse(self, value: str) -> str:
        ...


# Example service
class SimpleReverser(Reverser):
    def reverse(self, value: str) -> str:
        return value[::-1]


# Registering the service
DI.register_singleton(Reverser, SimpleReverser())


# Injecting the service to the view
@view.di
def index(request, reverser: Reverser):
    name = request.GET.get("name", "No name supplied")
    reversed_name = reverser.reverse(name)
    return HttpResponse(f"Hello, {html.escape(reversed_name)}!")


urlpatterns = [
    path("", index),
]

app = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
