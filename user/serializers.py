# from rest_framework import serializers

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=55)
    email_id = serializers.EmailField(max_length=500)
    password = serializers.CharField(max_length=30)
    account_type = serializers.CharField(max_length=10)

    """create function create to post data"""
    def create(self, validation_data):
        return User.objects.create(**validation_data)

    """create function update to put data"""
    def update(self, instance, validated_data):
        # instance.id = validated_data.get('id', instance.id)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email_id = validated_data.get('email_id', instance.email_id)
        instance.password = validated_data.get('password', instance.password)
        instance.account_type = validated_data.get('account_type', instance.account_type)
        # instance.created_at = validated_data.get('created_at', instance.created_at)
        # instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        
        instance.save()
        return instance

