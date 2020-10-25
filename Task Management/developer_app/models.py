from django.db import models
from django.contrib.auth.models import User

class TaskInfo(models.Model):

    assign_developer = models.ForeignKey(User,on_delete=models.CASCADE)
    task_details = models.CharField(max_length=400)
    manager_commit = models.CharField(max_length=400)
    user_commit = models.CharField(max_length=400)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.assign_developer + '->' + self.task_details

