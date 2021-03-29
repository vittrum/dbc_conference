from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, lastname, phone, password=None):
        if not email:
            raise ValueError('Email required!')
        if not name or not lastname:
            raise ValueError('Credentials required!')

        user = self.model(
            phone=email,
            name=name,
            lastname=lastname
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email=email, password=password,
                                name='superuser', lastname='superuser')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone

    class Meta:
        db_table = "users"