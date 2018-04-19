from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("predictor", views.index1, name="index1"),
    path("update/", views.update, name="update"),
    path("update1/", views.update1, name="update1"),
]
