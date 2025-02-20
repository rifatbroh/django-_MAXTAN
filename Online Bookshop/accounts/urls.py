from django.urls import path
from accounts.views import UserRegisterView, UserLoginView, UserProfileView, UserLogoutView, UserChangePasswordView, DepositMoneyView, UserUpdateProfileView

app_name= 'accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update-profile/', UserUpdateProfileView.as_view(), name='update_profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change_password'),
    path('deposit/', DepositMoneyView.as_view(), name='deposit'),
]
