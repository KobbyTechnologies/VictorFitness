from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,username,password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("username is required")
        user = self.model(
            email=self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,username,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user