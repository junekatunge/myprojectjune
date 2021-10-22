from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q

#from accounts.choices import ROLES_TYPE



class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_queryset(self):
        return super().get_queryset()

    def active(self):
        return self.get_queryset().filter(is_active=True)

    def inactive(self):
        return self.get_queryset().filter(is_active=False)

    def admins(self):
         return self.get_queryset().filter(Q(is_staff=True) | Q(is_superuser=True))

    def _create_user(
            self,
            user_email,
            f_name=None,
            l_name=None,
            password=None,
        **extra_fields
     ):
         user = self.model(
            user_email=user_email,
            f_name = f_name,
            l_name = l_name,
            **extra_fields
        )
         user.is_active = True
         if password:
            user.set_password(password)
            user.save(using=self._db)
            return user

    def get_by_natural_key(self, username):
        username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{username_field: username})

    def create_user(
        self,
        user_email,
        f_name=None,
        l_name=None,
        password=None,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_verified", True)
        return self._create_user(
            user_email, f_name, l_name, password, **extra_fields
        )


    def create_superuser(
        self,
        user_email,
        f_name=None,
        l_name=None,
        password=None,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(
            user_email, f_name, l_name, password, **extra_fields
        )
