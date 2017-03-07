from django.contrib import admin
from task.models import Task_Table, Announcements

# Register your models here.

admin.site.register(Task_Table)

admin.site.register(Announcements)