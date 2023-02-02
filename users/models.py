
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Поля :
    - аватар
    - номер телефона
    - страна
    """
    objects = CustomUserManager()

    username = None
    email = models.EmailField(verbose_name='почта',
                              unique=True
                              )
    phone = models.CharField(max_length=25,verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/',verbose_name='аватар')
    country = models.CharField(max_length=40,verbose_name='страна')
    token = models.CharField(max_length=15,verbose_name='токен',blank=True,null=True)
    token_created = models.DateTimeField(blank=True,null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


