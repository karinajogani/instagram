# from django.shortcuts import render
# from .models import Follow, User
# from .serializers import FollowSerializer
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.authentication import SessionAuthentication
# Create your views here.

# class Followapi(viewsets.ModelViewSet):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

from django.shortcuts import render
from rest_framework.response import Response
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.views import APIView


class FollowAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Follow.objects.get(id=id)
            serializer = FollowSerializer(stu)
            return Response(serializer.data)
            
        stu = Follow.objects.all()
        serializer = FollowSerializer(stu, many=True)
        return Response(serializer.data)   

    def post(self, request, format=None):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = Follow.objects.get(pk=id)
        serializer = FollowSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Complete Updated'})
        return Response(serializer.errors) 

    def patch(self, request, pk, format=None):
        id = pk
        stu = Follow.objects.get(pk=id)
        serializer = FollowSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Follow.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        