from django.urls import path
from .views import redirect_to_server

urlpatterns = [
    path("", redirect_to_server, name="redirection")
]