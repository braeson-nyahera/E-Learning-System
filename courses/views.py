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

def SearchView(request):
    if request.method == 'POST':
        search_name = request.POST.get('search')
        results = Course.objects.filter(title__contains=search_name)
        context = {
            'results':results
        }
        return render(request,'courses/search_result.html', context)