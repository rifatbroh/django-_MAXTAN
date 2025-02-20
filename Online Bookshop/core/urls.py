from django.urls import path
from core.views import home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("category/<slug:slug>/", home_view, name="category"),
]
