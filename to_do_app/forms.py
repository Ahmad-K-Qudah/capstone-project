from django import forms
from .models import  Task


# class UserFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['user_name','user_email']
#         error_messages = {
#             "user_name": {
#                 # "max_length": "Keep it short, please."
#             }
#         }        

class TaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','task_type','task_description','task_due_date','task_is_completed','user_id']
        widgets={
            'task_due_date':forms.DateInput(attrs={"type":"date","id":"date_id"}),
            # 'task_is_completed':forms.BooleanField(attrs={"type":"checkbox","id":"completed_id"})

        }
              