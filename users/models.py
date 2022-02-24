from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_field):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField('first_name', max_length=255, blank=True, null=True)
    last_name = models.CharField('last_name', max_length=255, blank=True, null=True)
    other_name = models.CharField('other_name', max_length=255, blank=True, null=True)
    email = models.CharField('email', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField('phone', blank=True, null=True)
    is_admin = models.BooleanField('is_admin', default=False)

    objects = MyUserManager()
