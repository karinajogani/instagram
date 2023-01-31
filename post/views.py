from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView

class PostAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Post.objects.get(id=id)
            serializer = PostSerializer(stu)
            return Response(serializer.data)
            
        stu = Post.objects.all()
        serializer = PostSerializer(stu, many=True)
        return Response(serializer.data)   

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = Post.objects.get(pk=id)
        serializer = PostSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Complete Updated'})
        return Response(serializer.errors) 

    def patch(self, request, pk, format=None):
        id = pk
        stu = Post.objects.get(pk=id)
        serializer = PostSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Post.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        