from django.urls import path

from . import views

urlpatterns = [
    path("encyclopedia", views.index, name="index"),
    path("newpage", views.nPage, name="NewPage")
]
