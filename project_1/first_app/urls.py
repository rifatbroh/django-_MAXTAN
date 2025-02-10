
from django.urls import path
from . import views 

# here calling function for access
urlpatterns = [
    path('courses/', views.courses),
    path('rifatbroh/', views.rifatbroh),
    path("", views.home),
    path('test/', views.test),
]
