# from django.shortcuts import render
from task.models import *
from rest_framework import viewsets
from task.serializers import *
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import django_filters

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

        num_completed = len([task['completed'] for task in data if task['completed'] == True])
        buffer_time = 15*60 #minutes*seconds
        num_on_time = len([task['completed'] for task in data if
                           task['completed'] == True and task['deadline_timestamp']+buffer_time >= task['last_modified_timestamp']])
        num_late = len([task['completed'] for task in data if
                           task['completed'] == True and task['deadline_timestamp']+buffer_time < task['last_modified_timestamp']])
        num_unfinished = len([task['completed'] for task in data if task['completed'] == False])

        stats = {'num_completed': num_completed, 'num_on_time': num_on_time, 'num_late': num_late, 'num_unfinished': num_unfinished,}
        # test = len([task for task in data if task['types']=='CLEANING'])
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            # ('num_completed', num_completed),
            # ('num_on_time', num_on_time),
            # ('num_late', num_late),
            # ('num_unfinished', num_unfinished),
            ('stats', stats),
            ('type_counts', type_counts),
            # ('cleaning', test),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
        ]))

class TaskFilter(FilterSet):
    created_timestamp = django_filters.NumberFilter(name='created_timestamp', lookup_expr='exact')
    start = django_filters.NumberFilter(name='created_timestamp', lookup_expr='gte')
    end = django_filters.NumberFilter(name='created_timestamp', lookup_expr='lte')

    class Meta:
        model = Task_Table
        fields = ['label', 'completed', 'designee', 'types', 'created_timestamp', 'start', 'end',]


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
    # filter_fields = ('label', 'completed', 'designee', 'types')
    filter_class = TaskFilter
    pagination_class = TaskPagination


    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    @list_route(methods=['get'])
    def test_view(self, request):
        queryset = Task_Table.objects.all()
        cleaning_count = (Task_Table.objects.filter(types='CLEANING').count())
        serializer = self.get_serializer(queryset, many=True)
        # self.request.data
        try:
            print('DFKJDSHFDKFJDFKDSJFHDKSHFKSFHASDFHDSF')
            print(self.request.query_params)
            return Response(self.request.query_params)
        except:
            return Response('bye')
        # return Response(serializer.data)

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


class SharedTasksViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
    """
    queryset = SharedTasks.objects.all()
    serializer_class = SharedTasksSerializer