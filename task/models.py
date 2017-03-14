from django.db import models

# Create your models here.

class Task_Table(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    last_modified = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    label = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(default='')
    designee = models.CharField(max_length=50, blank=True)
    # started_time = models.DateTimeField(auto_now_add=True)
    # completed_time = models.DateTimeField(blank=True, default='')
    CHOICES_OF_TYPE = (
        ('OTHERS', 'Others'),
        ('CLEANING', 'Cleaning'),
        ('COMPUTER', 'Computer Work'),
        ('DELIVERY', 'Delivery'),
        ('TRAVEL', 'Travel'),
    )
    types = models.CharField(max_length=15, choices=CHOICES_OF_TYPE,
                             default='OTHERS')

    class Meta:
        ordering = ('created',)

    def started_time_pretty(self):
        return self.started_time.strftime('%b %e %Y')

    def completed_time_pretty(self):
        return self.completed_time.strftime('%b %e %Y')


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