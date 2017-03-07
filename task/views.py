from django.shortcuts import render
from task.models import Task_Table, Announcements
from rest_framework import viewsets
from task.serializers import TaskSerializer, AnnoucementsSerializer



# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Task_Table.objects.all()
    serializer_class = TaskSerializer
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

    def perform_create(self, serializer):
        serializer.save()

