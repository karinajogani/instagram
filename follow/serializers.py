from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.Serializer):
    id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    following_id = serializers.ForeignKey(User, on_delete=models.CASCADE)
    created_by = serializers.CharField()
    updated_by = serializers.CharField()
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)
    is_delete = serializers.BooleanField(default=True)
