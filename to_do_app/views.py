from django.shortcuts import render, redirect
from django.urls import reverse
from .models import  Task
from .forms import  TaskFrom
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm #form to create  new user
from django.contrib.auth.models import User # built in User model
from django.contrib.auth.mixins import LoginRequiredMixin


def homepage(request):
    return render(request,'homepage.html')

class SignUpView(CreateView):
    model = User
    form_class= UserCreationForm
    success_url = '/auth/login'
    template_name = 'registration/signup.html'


class TaskListView(LoginRequiredMixin,ListView):
    model=Task
    template_name='task/task-list.html'
    context_object_name='all_tasks'
    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class TaskDetailedView(LoginRequiredMixin,DetailView):
    model=Task
    template_name='task/task-details.html'
    context_object_name='task'
    pk_url_kwarg='id'

class TaskCreateView(LoginRequiredMixin,CreateView):
    model=Task
    form_class=TaskFrom
    template_name='task/task-form.html'
    success_url=reverse_lazy('all_tasks')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context    
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Task
    form_class=TaskFrom
    template_name='task/task-form.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('all_tasks')


    
    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('all_tasks')


