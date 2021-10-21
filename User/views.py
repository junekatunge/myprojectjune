from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import Userserialer
from rest_framework.permissions import AllowAny



class UserViewSet (ModelViewSet):#a viewset that provides methodss for updating,deleting,creating actions
    serializer_class= Userserialer
    queryset= User.objects.all()
    permission_classes = (AllowAny,)#overrride the global permission,hence locally defined permission is used
# Create your views here.
 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

User = get_user_model()

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = Userserialer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames =  User.objects.all()
        # usernames = None
        serializer = self.serializer_class(usernames,many=True)
        return Response(serializer.data)


# for custom authentication by token

class CustomAuthToken(ObtainAuthToken):

    permission_classes=(AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })