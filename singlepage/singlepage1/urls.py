from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.index, name="index"),
    path('section/<int:num>', views.section, name="section"),
]