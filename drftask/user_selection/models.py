from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager


# Модель хранящяя данные каждой роли
class Role(models.Model):
     name = models.CharField(max_length=255)
     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

     def __str__(self):
          return self.name


# Расширение стандартной модели User полями offer, role_choice
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    offer = models.BooleanField(default=False)
    role_choice = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
