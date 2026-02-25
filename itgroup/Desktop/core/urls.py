from django.urls import path
from . import views

urlpatterns = [

    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("products/", views.products_view, name="products"),

    path("products/networking/", views.networking_view, name="networking"),
    path("products/security/", views.security_view, name="security"),
    path("products/wireless/", views.wireless_view, name="wireless"),
    path("products/software/", views.software_view, name="software"),

    path("solutions/", views.solutions_view, name="solutions"),

    path("contact/", views.contact_view, name="contact"),
    path("careers/", views.careers_view, name="careers"),
]