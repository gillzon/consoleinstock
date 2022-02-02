from django.urls.conf import include
from django.conf.urls import url
from django.urls import path
from api.views import home

app_name = "api"

urlpatterns = [
    path('', home, name="index"),
]
