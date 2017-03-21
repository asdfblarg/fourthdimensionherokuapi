# from django.shortcuts import render
from task.models import *
from rest_framework import viewsets
from task.serializers import *
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class TaskPagination(PageNumberPagination):
#     page_size = 1
    def get_paginated_response(self, data):
        task_types = [task['types'] for task in data]
        type_counts = {}
        for type in task_types:
            type_counts[type] = type_counts.get(type, 0) + 1

        test = len([task for task in data if task['types']=='CLEANING'])
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('type_counts', type_counts),
            # ('cleaning', test),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
        ]))


# Create your views here.

from django.db.models import Count
from rest_framework.decorators import list_route

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Task_Table.objects.all()
    # print(Task_Table.objects.filter(types='CLEANING').count())
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('label', 'completed', 'designee', 'types',)
    pagination_class = TaskPagination


    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    @list_route(methods=['get'])
    def test_view(self, request, **kwargs):
        queryset = Task_Table.objects.all()
        cleaning_count = (Task_Table.objects.filter(types='CLEANING').count())

        return Response({'cleaning' : cleaning_count,})

    # def get_queryset(self):
    #     return Task_Table.objects.annotate(cleaning_count = Count('types'))


# class DerpViewSet(viewsets.ViewSet):
#     queryset = Task_Table.objects.order_by('types')
#     # serializer_class = TaskSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('label', 'completed', 'designee', 'types',)
#     pagination_class = TaskPagination


class AnnouncementsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Announcements.objects.all()
    serializer_class = AnnoucementsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('label', 'seen')


class UsersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'firebaseid', 'email')


class WeekScheduleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = WeekSchedule.objects.all()
    serializer_class = WeekScheduleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('firebaseid', 'week_num', 'year', )


