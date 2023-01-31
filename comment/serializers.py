from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'type', 'type_id', 'created_by', 'comment', 'created_at', 'updated_at')