from django.contrib import admin
from django.contrib.admin import ModelAdmin
from developer_app.models import TaskInfo


admin.site.site_header = 'Manager Login'

class AdminTaskInfo(ModelAdmin):

    list_display = ['id','assign_developer','task_details','manager_commit','user_commit','status']
    list_filter = ('assign_developer', 'status')
    class Meta:
        model = TaskInfo

admin.site.register(TaskInfo,AdminTaskInfo)