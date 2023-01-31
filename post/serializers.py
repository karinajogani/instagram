from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','photo','caption', 'created_by', 'created_at', 'updated_at')


#  'updated_by',