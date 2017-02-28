from django.shortcuts import render
from task.models import Task_Table
from rest_framework import viewsets
from task.serializers import TaskSerializer



# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task_Table.objects.all()
    serializer_class =TaskSerializer


####

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response


from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })

# from rest_framework.decorators import detail_route

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Task_Table.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        serializer.save()



