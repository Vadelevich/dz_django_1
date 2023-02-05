from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView
from django.urls import path

from users.apps import UsersConfig

from users.views import CustomLoginView, UserEditProfileView, CustomRegisterView, user_activation, ResetPasswordView, \
    SignupSuccessView

app_name = UsersConfig.name




urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('activate/<str:token>/',user_activation, name='activate'),
    path('reset/',ResetPasswordView.as_view(), name='reset'),
    path('register/success/', SignupSuccessView.as_view(), name='register_success'),
    path('reset/success/', SignupSuccessView.as_view(), name='reset_success'),
]
