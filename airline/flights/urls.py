from django.urls import include, path
from . import views

app_name = "flights"
urlpatterns = [
    path("", views.index, name="index"),
]
