from django.urls import path
from . import views

urlpatterns = [
    path('cse/', views.CSE),
    path('eee/', views.EEE),
    path('civil/', views.Cvil),
    path('eng/', views.ENG),
    path('bba/', views.BBA),

]
