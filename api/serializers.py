from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    is_read = serializers.BooleanField()
    class Meta:
        model = Message
        fields = '__all__'