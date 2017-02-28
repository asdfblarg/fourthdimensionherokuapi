from rest_framework import serializers
from task.models import Task_Table

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task_Table
        # fields = ( 'url', 'id', 'created', 'title', 'last_modified', 'completed',
        #     'label','description','designee','started_time','completed_time','types')

        fields = ('url',
                  'id',
                  'created',
                  'completed',
                  'label',
                  'description',
                  'designee',
                  'types',
                  # 'completed_time',
                  'last_modified',
                  )
