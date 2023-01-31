from rest_framework import serializers
from .models import Story
from user.serializers import UserSerializer

class StorySerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True)
    views =UserSerializer(many=True)

    class Meta:
        model = Story
        fields = ('id', 'image', 'title', 'created_by', 'viewed_by', 'created_at', 'expires_at')