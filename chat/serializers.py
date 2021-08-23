from rest_framework import serializers

from .models import Message


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        exclude = ['updated_at']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
