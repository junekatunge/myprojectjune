from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

#for authentication token generation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from User.managers import UserManager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    f_name=models.CharField(max_length=100, null=False)
    l_name=models.CharField(max_length=100, null= False)
    user_email=models.EmailField(max_length=254, unique=True)
    gender=models.CharField(choices=(('m','male'),('f','female')),max_length=1)
    #what the system will use to check during login 
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS=['f_name', 'l_name']

    objects=UserManager()

