from django.db import models
from dateutil.parser import parse
import datetime

# Create your models here.

# class Task_Table_List(models.Model):
#     pass
#     # tasks_list = models.ForeignKey(Task_Table, on_delete=models.CASCADE)
#     def get_queryset(self):
#         return super(Task_Table_Manager, self).get_queryset().annotate(cleaning_count = models.Count('types'))

class Task_Table(models.Model):
    # task_list = models.ForeignKey(Task_Table_List, related_name='tasks_list' , null=True)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    last_modified = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    label = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(default='')
    designee = models.CharField(max_length=50, blank=True)
    # created_timestamp = models.IntegerField(editable=False, default=123)
    created_timestamp = models.IntegerField(null=True, editable=False)
    last_modified_timestamp = models.IntegerField(null=True, editable=False)

    CHOICES_OF_TYPE = (
        ('OTHERS', 'Others'),
        ('CLEANING', 'Cleaning'),
        ('COMPUTER', 'Computer Work'),
        ('DELIVERY', 'Delivery'),
        ('TRAVEL', 'Travel'),
    )
    types = models.CharField(max_length=15, choices=CHOICES_OF_TYPE,
                             default='OTHERS')

    # objects = models.Manager()
    # cleaning_objects = Task_Table_Manager()

    class Meta:
        ordering = ('created',)

    # def created_timestamp(self):
    #     return self.created.timestamp()
    # def last_modified_timestamp(self):
    #     return self.last_modified.timestamp()

    def save(self, *args, **kargs):
        if not self.created:# created is none before model is first created
            self.created_timestamp = int(datetime.datetime.now().timestamp())
        else:
            self.created_timestamp = int(self.created.timestamp())


        super(Task_Table, self).save(*args, **kargs)
        try:
            self.last_modified_timestamp = int(self.last_modified.timestamp())
        except:
            self.last_modified_timestamp = int(datetime.datetime.now().timestamp())

    #
    # def create(self, *args, **kargs):
    #     super(Task_Table, self).create(*args, **kargs)
    #     # self.created_timestamp = int(self.created.timestamp())
    #     # self.last_modified_timestamp = int(self.last_modified.timestamp())



class Announcements(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    seen = models.BooleanField(default=False)
    label = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(default='')

    class Meta:
        ordering = ('created',)


class Users(models.Model):
    name = models.CharField(max_length = 50, blank=True, default='')
    firebaseid = models.CharField(max_length=200, blank=True, default='')
    email = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

class WeekSchedule(models.Model):
    firebaseid = models.CharField(max_length=300, blank=True, default='')
    week_num = models.IntegerField()
    year = models.IntegerField()
    mon_start = models.CharField(max_length=20, blank=True, default='')
    mon_end = models.CharField(max_length=20, blank=True, default='')
    tues_start = models.CharField(max_length=20, blank=True, default='')
    tues_end = models.CharField(max_length=20, blank=True, default='')
    wed_start = models.CharField(max_length=20, blank=True, default='')
    wed_end = models.CharField(max_length=20, blank=True, default='')
    thurs_start = models.CharField(max_length=20, blank=True, default='')
    thurs_end = models.CharField(max_length=20, blank=True, default='')
    fri_start = models.CharField(max_length=20, blank=True, default='')
    fri_end = models.CharField(max_length=20, blank=True, default='')
    sat_start = models.CharField(max_length=20, blank=True, default='')
    sat_end = models.CharField(max_length=20, blank=True, default='')
    sun_start = models.CharField(max_length=20, blank=True, default='')
    sun_end = models.CharField(max_length=20, blank=True, default='')


    class Meta:
        ordering = ('id',)