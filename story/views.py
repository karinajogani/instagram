from django.shortcuts import render
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer
from rest_framework.views import APIView

class StoryAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Story.objects.get(id=id)
            serializer = StorySerializer(stu)
            return Response(serializer.data)
            
        stu = Story.objects.all()
        serializer = StorySerializer(stu, many=True)
        return Response(serializer.data)   

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = Story.objects.get(pk=id)
        serializer = StorySerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Complete Updated'})
        return Response(serializer.errors) 

    def patch(self, request, pk, format=None):
        id = pk
        stu = Story.objects.get(pk=id)
        serializer = StorySerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Story.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        