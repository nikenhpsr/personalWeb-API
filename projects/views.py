from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Project, ProjectMedia
from .serializers import ProjectInputSerializer, ProjectOutputSerializer, ProjectUpdateSerializer, ProjectMediaInputSerializer, ProjectMediaSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectInputSerializer
        elif self.action in ['update', 'partial_update']:
            return ProjectUpdateSerializer
        return ProjectOutputSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        output_serializer = ProjectOutputSerializer(instance=serializer.instance)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"detail": "You do not have permission to edit this project."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"detail": "You do not have permission to delete this project."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class ProjectMediaViewSet(viewsets.ModelViewSet):
    queryset = ProjectMedia.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectMediaInputSerializer
        return ProjectMediaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.validated_data['project']
        if project.user != request.user:
            return Response({"detail": "You do not have permission to add media to this project."},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.project.user != request.user:
            return Response({"detail": "You do not have permission to delete this media."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)