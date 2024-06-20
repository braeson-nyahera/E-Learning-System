from django.shortcuts import render
from .models import Subject, Course, Content,Module
from django.views.generic import ListView,DetailView,TemplateView

# Create your views here.
class CourseListView(ListView):
    model=Course
    template_name='courses/courses.html'
    context_object_name='courses'
    ordering=['-created']

class CourseDetailView(DetailView):
    model=Course
    template_name='courses/course_detail.html'
    
class ModuleDetailView(DetailView):
    model=Module
    template_name='courses/module_detail.html'
