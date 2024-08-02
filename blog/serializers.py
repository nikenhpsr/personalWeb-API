from rest_framework import serializers
from .models import Blog, BlogMedia

class BlogMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMedia
        fields = ['id', 'file']

class BlogInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'tags', 'content']

class BlogOutputSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    media = BlogMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'tags', 'publication_date', 'content', 'media']

class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'tags', 'content']
        extra_kwargs = {'title': {'required': False}, 'tags': {'required': False}, 'content': {'required': False}}

class BlogMediaInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMedia
        fields = ['blog', 'file']