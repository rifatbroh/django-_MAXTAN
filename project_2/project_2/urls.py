
from django.contrib import admin
from django.urls import path, include
# view page theke import kortesi as a user response
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('test/', views.test),
    path('map/', views.map),

    path('first_app/', include("first_app.urls")),
]
