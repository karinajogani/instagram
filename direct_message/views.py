from django.shortcuts import render
from rest_framework.response import Response
from .models import DirectMessage
from .serializers import DirectMessageSerializer
from rest_framework.views import APIView

class DirectMessageAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = DirectMessage.objects.get(id=id)
            serializer = DirectMessageSerializer(stu)
            return Response(serializer.data)
            
        stu = DirectMessage.objects.all()
        serializer = DirectMessageSerializer(stu, many=True)
        return Response(serializer.data)   

    def post(self, request, format=None):
        serializer = DirectMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = DirectMessage.objects.get(pk=id)
        serializer = DirectMessageSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Complete Updated'})
        return Response(serializer.errors) 

    def patch(self, request, pk, format=None):
        id = pk
        stu = DirectMessage.objects.get(pk=id)
        serializer = DirectMessageSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = DirectMessage.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        