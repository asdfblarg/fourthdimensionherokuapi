from rest_framework import serializers, pagination
from task.models import *#Task_Table, Announcements, Users, WeekSchedule


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # created_timestamp = serializers.CharField()#source='created_timestamp')
    # last_modified_timestamp = serializers.CharField()#source='last_modified_timestamp')

    class Meta:
        model = Task_Table
        # fields = ( 'url', 'id', 'created', 'title', 'last_modified', 'completed',
        #     'label','description','designee','started_time','completed_time','types')

        # created_timestamp = serializers.CharField()  # source='created_timestamp')
        last_modified_timestamp = serializers.IntegerField()  # source='last_modified_timestamp')

        # created_timestamp = serializers.ReadOnlyField()
        # last_modified_timestamp = serializers.ReadOnlyField()
        fields = ('url',
                  'id',
                  'created',
                  'created_timestamp',
                  'completed',
                  'label',
                  'description',
                  'designee',
                  'types',
                  'last_modified',
                  'last_modified_timestamp',
                  )



# bad
# # class TaskCountField(serializers.Field):
# #     def to_native(self, types):
# #
# #         counts = {
# #             '1_mile': self._cleaning_counts(types)
# #         }
# #
# #
# #         return counts
# #
# #     def _cleaning_counts(self, tasks):
# #         return tasks.filter(types='CLEANING').count()
# #
# # class TaskTypesSerializer(pagination.PaginationSerializer):
# #     # """
# #     # Serializes page objects of user querysets.
# #     # """
# #     distance_counts = TaskCountField(source='paginator.object_list')
# #     class Meta:
# #         object_serializer_class = TaskSerializer

# class TaskTypesSerializer(serializers.Serializer):
#     # # queryset = Task_Table.objects.order_by('types')
#     # test = serializers.SerializerMethodField()
#     # # serializers.IntegerField(
#     # #     source='user_set.count',
#     # #     read_only=True
#     # # )
#     # class Meta:
#     #     # model = Task_Table
#     #     fields = ('id', 'test')
#     #
#     # def get_test(self, obj):
#     #     return obj.types.count('CLEANING')
#     pass


# class GroupSerializer(serializers.ModelSerializer):
#
#     user_count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Group
#         fields = ('id', 'name','user_count')
#
#     def get_user_count(self, obj):
#         return obj.user_set.count()


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
