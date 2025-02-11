from django.urls import path
from . import views

urlpatterns = [
    path('first_app/', views.app),
]
