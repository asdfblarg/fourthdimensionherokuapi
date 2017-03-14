from rest_framework import serializers
from task.models import Task_Table, Announcements, Users

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

class AnnoucementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcements
        fields = (
                    'url',
                    'id',
                    'created',
                    'seen',
                    'label',
                    'description',
                    'last_modified',
                  )

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = (
                    'url',
                    'id',
                    'name',
                    'firebaseid',
                    'email',
                  )
