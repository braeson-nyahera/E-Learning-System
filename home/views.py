from django.shortcuts import render
from courses.models import Subject, Course
from django.views.generic import ListView

# Create your views here.

class CourseListView(ListView):
    model=Course
    template_name='home/home.html'
    context_object_name='courses'

def landing(request):
    return render(request,'home/landing.html')

def base(request):
    return render(request,'home/base.html')

def home(request):

    return render(request, 'home/home.html')