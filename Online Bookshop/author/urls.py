from django.urls import path
from author.views import AuthorProfileView

urlpatterns = [
    path('<int:pk>/', AuthorProfileView.as_view(), name='author_profile'),
]

