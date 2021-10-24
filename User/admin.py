from django.contrib import admin
from django.db import models

from User.models import User
from .models import User
# Register your models here.
admin.site.register(User)