from django.shortcuts import render
from .models import Student
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'CRUDApp/home.html'

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/cbv/list/'

class StudentListView(ListView):
    model = Student

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/cbv/list/'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/cbv/list/'


    


