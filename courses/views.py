from django.shortcuts import render, redirect
from .models import Subject, Course, Content,Module
from django.views.generic import ListView,DetailView,TemplateView
from .forms import SubjectForm,CourseForm, ContentForm, ModuleForm

# Create your views here.
def AddCourseView(request):
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        course_form = CourseForm(request.POST)
        content_form = ContentForm(request.POST)
        module_form = ModuleForm(request.POST)

        if subject_form.is_valid() and course_form.is_valid() and content_form.is_valid() and module_form.is_valid():
            subject_form.save()
            course_form.save()
            content_form.save()
            module_form.save()
            return redirect('courses')

    else:
        subject_form = SubjectForm()
        course_form = CourseForm()
        content_form = ContentForm()
        module_form = ModuleForm()

    context = {
        'subject_form': subject_form,
        'course_form': course_form,
        'content_form': content_form,
        'module_form': module_form,
    }

    return render(request, 'courses/add_course.html', context)

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