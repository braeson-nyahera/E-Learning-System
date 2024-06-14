from django.shortcuts import render
from .models import Subject
from django.views.generic import ListView,DetailView

# Create your views here.
class SubjectListView(ListView):
    model=Subject
    template_name='courses/courses.html'
    context_object_name='subjects'

class SubjectDetailView(DetailView):
    model=Subject
    template_name='courses/course_detail.html'