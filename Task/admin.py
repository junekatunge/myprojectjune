from django.contrib import admin
from .models import Task, AssignTask

# Register your models here.
admin.site.register(Task)
admin.site.register(AssignTask)