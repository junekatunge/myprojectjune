from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import AssignTask, Task

class TaskSerializer(ModelSerializer):

    class Meta:#here we choose the model to be serialized by the modelserializer
        model=Task, AssignTask
        fields='__all__'#i want all the fields in the User model to be serialized 

# class AssignTaskSerailizer(ModelSerializer):

    # class Meta:
        # model=AssignTask
        # fields='__all__'