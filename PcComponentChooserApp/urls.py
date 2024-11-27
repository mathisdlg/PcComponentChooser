from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/<str:next_page>", views.register_login_page, name="register", kwargs={"clicked": "register"}),
    path("register", views.register_login_page, name="register", kwargs={"clicked": "register"}),
    path("login/<str:next_page>", views.register_login_page, name="login", kwargs={"clicked": "login"}),
    path("login", views.register_login_page, name="login", kwargs={"clicked": "login"}),
    path("logout", views.logout_view, name="logout"),

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
    path("builder", views.wip, name="builder"),
]