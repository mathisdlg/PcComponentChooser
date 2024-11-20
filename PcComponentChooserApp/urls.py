from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # WIP path
    path("wip", views.wip, name="wip"),
    path("cpu", views.wip, name="cpu"),
    path("cpu_cooler", views.wip, name="cpu_cooler"),
    path("gpu", views.wip, name="gpu"),
    path("ram", views.wip, name="ram"),
    path("motherboard", views.wip, name="motherboard"),
    path("storage", views.wip, name="storage"),
    path("psu", views.wip, name="psu"),
    path("cooling", views.wip, name="cooling"),
    path("case", views.wip, name="case"),
    path("monitor", views.wip, name="monitor"),
    path("peripherals", views.wip, name="peripherals"),
    path("profile", views.wip, name="profile"),

]