from rest_framework import serializers
from task.models import Task_Table, Announcements, Users, WeekSchedule

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

class WeekScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeekSchedule
        fields = (
                    'url',
                    'id',
                    'firebaseid',
                    'week_num',
                    'year',
                    'mon_start',
                    'mon_end',
                    'tues_start',
                    'tues_end',
                    'wed_start',
                    'wed_end',
                    'thurs_start',
                    'thurs_end',
                    'fri_start',
                    'fri_end',
                    'sat_start',
                    'sat_end',
                    'sun_start',
                    'sun_end',
                  )
