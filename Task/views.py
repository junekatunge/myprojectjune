from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializer import TaskSerializer
from .models import Task, AssignTask
from rest_framework.authentication import TokenAuthentication


class TaskViews(APIView):
    authentication_classes = [TokenAuthentication,]
    serializer_class= TaskSerializer
    permission_classes= (IsAuthenticated,)



    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        print(self.request.user.id)
        queryset = AssignTask.objects.filter(user= self.request.user.id)
        # serializer = AssignTaskSerailizer(queryset.many=True).data
        return Response({})
