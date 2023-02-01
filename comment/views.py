from django.shortcuts import render
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView

class CommentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Comment.objects.get(id=id)
            serializer = CommentSerializer(stu)
            return Response(serializer.data)
            
        stu = Comment.objects.all()
        serializer = CommentSerializer(stu, many=True)
        return Response(serializer.data)   

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.type)
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = Comment.objects.get(pk=id)
        serializer = CommentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Complete Updated'})
        return Response(serializer.errors) 

    def patch(self, request, pk, format=None):
        id = pk
        stu = Comment.objects.get(pk=id)
        serializer = CommentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Comment.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        