from django.contrib.auth.base_user import AbstractBaseUser# model that contains the authentication functionality
from django.contrib.auth.models import PermissionsMixin# adds superuser and user_permissions functionality
from django.db import models

#for authentication token generation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from User.managers import UserManager
from django.utils.translation import ugettext_lazy as _ #translation function to translate to the end user language

#to receive a signal that token has been assigned 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    f_name=models.CharField(_("first name"),max_length=100, null=False)
    l_name=models.CharField(_("last name"),max_length=100, null= False)
    user_email=models.EmailField(_("email"),max_length=254, unique=True)
    gender=models.CharField(_("gender"),choices=(('m','male'),('f','female')),max_length=1)
    is_staff = models.BooleanField(_("staff status"),default=False) #loging part
    is_active = models.BooleanField(_("active"),default=False)
    is_verified = models.BooleanField(_("verified"),default=False)
    # token= models.ForeignKey (Token, on_delete=models.CASCADE)

    #what the system will use to check during login 
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS=['f_name', 'l_name']

    objects=UserManager()#class for managing users has been assigned to a variable 

