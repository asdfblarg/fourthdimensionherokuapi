from django.contrib import admin
from task.models import Task_Table, Announcements, Users

# Register your models here.

admin.site.register(Task_Table)

admin.site.register(Announcements)
admin.site.register(Users)