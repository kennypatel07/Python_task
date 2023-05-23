from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserList(APIView):
    
    def get(self,request,format=None):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=True):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetail(APIView):
    
    def delete(self,request,pk,format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message':'User Deleted'})
    