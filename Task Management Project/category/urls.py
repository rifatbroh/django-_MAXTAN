from django.urls import path
from category import views

urlpatterns = [
    path('add/', views.add_category, name='add_category'),
]
