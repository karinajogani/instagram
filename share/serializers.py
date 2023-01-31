from rest_framework import serializers
from .models import Share
from user.serializers import UserSerializer

class ShareSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True)
    share =UserSerializer(many=True)

    class Meta:
        model = Share
        fields = ('id','type', 'type_id', 'created_by', 'share_to', 'created_at', 'updated_at')