from django.shortcuts import render
from .models import Subject, Course, Content,Module
from django.views.generic import ListView,DetailView,TemplateView

# Create your views here.
class SubjectListView(TemplateView):
    template_name='courses/courses.html'

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            "subjects": Subject.objects.all(),
            "courses": Course.objects.all(),
        }
        return self.render_to_response(self.extra_context)

class SubjectDetailView(TemplateView):
    template_name='courses/course_detail.html'

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            "subjects": Subject.objects.all(),
            "courses": Course.objects.all(),
            "contents":Content.objects.all(),
            "modules":Module.objects.all(),
        }
        return self.render_to_response(self.extra_context)
    
class ModuleDetailView(DetailView):
    model=Module
    template_name='courses/module_detail.html'
