from rest_framework import serializers
from .models import Project, ProjectMedia

class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = ['id', 'media_type', 'media_link']

class ProjectInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'tech_stack', 'description']

class ProjectOutputSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    media = ProjectMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'user', 'title', 'tech_stack', 'description', 'media']

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'tech_stack', 'description']
        extra_kwargs = {'title': {'required': False}, 'tech_stack': {'required': False}, 'description': {'required': False}}

class ProjectMediaInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = ['project', 'media_type', 'media_link']