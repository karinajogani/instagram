from rest_framework import serializers
from .models import DirectMessage
from user.serializers import UserSerializer

class DirectMessageSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True)
    send =UserSerializer(many=True)

    class Meta:
        model = DirectMessage
        fields = ('id','message', 'created_by', 'send_to', 'created_at', 'updated_at')
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}    