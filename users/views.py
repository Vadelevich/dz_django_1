import datetime

import pytz as pytz
from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, TemplateView
from users.forms import CustomEditUserForm, CustomUserCreationForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_success')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
            self.object.token = User.objects.make_random_password(length=20)
            print(self.object.token)
            self.object.token_created = datetime.datetime.now().astimezone()
            self.object.is_active = False
            send_mail(
                subject='Активация',
                message=f' http://127.0.0.1:8000/users/activate/{self.object.token}/',


                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email],
                fail_silently=False,

            )
            self.object.save()
        return super().form_valid(form)


def user_activation(request,token):
    u = User.objects.filter(token=token)

    return redirect(reverse('catalog:home'))


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user


class ResetPasswordView(PasswordResetView):
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('users:reset_success')

class SignupSuccessView(TemplateView):
    template_name = 'users/signup_success.html'

class VerifySuccessView(TemplateView):
    template_name = 'users/verify_success.html'

