from rest_framework import serializers
from .models import Blog
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user_name')
    image = serializers.ImageField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'info', 'author', 'image']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'user_name', 'posts']
    
class SearchSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user_name')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'info', 'author', 'image']
