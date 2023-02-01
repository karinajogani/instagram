from rest_framework import serializers
from .models import Reels
from user.serializers import UserSerializer

class ReelSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True)
    views =UserSerializer(many=True)

    class Meta:
        model = Reels
        fields = ('reels_id', 'video', 'caption', 'created_by', 'viewed_by', 'created_at', 'updated_at')