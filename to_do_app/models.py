from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    task_name=models.CharField(max_length=30,null=False)
    task_type=models.CharField(max_length=30,null=False)
    task_description=models.TextField(null=True)
    task_due_date=models.DateField(null=True)
    task_is_completed=models.BooleanField(default=False)
    user_id=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='tasks')

    def __str__(self):
        return self.task_name
    
    class Meta:
        db_table = 'tasks'