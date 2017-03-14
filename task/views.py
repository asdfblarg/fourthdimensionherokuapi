from django.shortcuts import render
from task.models import Task_Table, Announcements, Users
from rest_framework import viewsets
from task.serializers import TaskSerializer, AnnoucementsSerializer, UsersSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Task_Table.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('label', 'completed', 'designee')

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        serializer.save()

class AnnouncementsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Announcements.objects.all()
    serializer_class = AnnoucementsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('label', 'seen')

    def perform_create(self, serializer):
        serializer.save()


class UsersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'firebaseid', 'email')

    def perform_create(self, serializer):
        serializer.save()

