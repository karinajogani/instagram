from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.Serializer):
    class Meta:
        model = Follow
        fields = ('id', 'following', 'created_by', 'created_at', 'updated_at')
