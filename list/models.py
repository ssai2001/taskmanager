from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task_name = models.CharField(max_length=30)
    task_description = models.TextField(max_length=150)
    task_status = models.BooleanField(default=False)

    class Meta:
        db_table = "task"