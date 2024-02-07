from .models import Posts
from rest_framework import serializers
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'body', 'owner', 'created_at', 'created_since']