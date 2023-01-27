from rest_framework import serializers
from .models import Post
# from django.conf import settings
# import uuid

# class Post(serializers.Serializer):
#     # id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     photo = serializers.ImageField()
#     caption = serializers.CharField(blank=True)
#     created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
#     updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
#     created_at = serializers.DateTimeField(auto_now_add=True)
#     updated_at = serializers.DateTimeField(auto_now=True)
#     is_deleted = serializers.BooleanField(default=False)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','photo','caption', 'created_by', 'updated_by')


