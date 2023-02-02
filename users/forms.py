from django.contrib.auth.forms import UserChangeForm, UserCreationForm,PasswordResetForm
from catalog.forms_mixins import StyleFormMixin
from users.models import User

class CustomEditUserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserCreationForm(StyleFormMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)



