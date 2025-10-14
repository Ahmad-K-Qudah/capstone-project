from django.urls import path
from . import views

urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('auth/signup/',views.SignUpView.as_view(),name='signup'),
   path('task/list/',views.TaskListView.as_view(),name='all_tasks'),
   path('task/<int:id>/',views.TaskDetailedView.as_view(),name="task_details"),
   path('task/create/',views.TaskCreateView.as_view(),name="task_create"),
   path('task/<int:id>/update/',views.TaskUpdateView.as_view(),name="task_update"),
   path('task/<int:id>/delete/',views.TaskDeleteView.as_view(),name="task_delete"),

]
