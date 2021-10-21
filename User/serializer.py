from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import User

class Userserialer (ModelSerializer):
    class Meta:#here we choose the model to be serialized by the modelserializer
        model=User
        fields='__all__'#i want all the fields in the User model to be serialized 

