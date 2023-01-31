from django.shortcuts import render
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from rest_framework.views import APIView

class LikeAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Like.objects.get(id=id)
            serializer = LikeSerializer(stu)
            return Response(serializer.data)
            
        stu = Like.objects.all()
        serializer = LikeSerializer(stu, many=True)
        return Response(serializer.data)   

    def post(self, request, format=None):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = Like.objects.get(pk=id)
        serializer = LikeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Complete Updated'})
        return Response(serializer.errors) 

    def patch(self, request, pk, format=None):
        id = pk
        stu = Like.objects.get(pk=id)
        serializer = LikeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Like.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        