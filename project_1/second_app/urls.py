
from django.urls import path
from . import views 

# here calling function for access
urlpatterns = [
    path('', views.front),
    path('about/', views.about),
    path('testomonial', views.testomonial),
    path('contact/', views.contact),
]
