from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User= get_user_model()
# Create your models here.
class Task(models.Model):
    title= models.TextField()
    description = models.TextField()
    start_time= models.TimeField()
    end_time= models.TimeField()
class AssignTask(models.Model):
    task= models.ForeignKey(Task, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)




