# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("cv/", views.download_cv, name='cv'),
]