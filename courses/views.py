from django.shortcuts import render
from .models import Subject, Course, Content,Module
from django.views.generic import ListView,DetailView,TemplateView

# Create your views here.
class SubjectListView(ListView):
    model=Subject
    template_name='courses/courses.html'
    context_object_name='subjects'

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