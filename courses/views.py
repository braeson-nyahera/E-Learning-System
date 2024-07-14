from django.shortcuts import render, redirect
from .models import Subject, Course, Content,Module
from django.views.generic import ListView,DetailView,TemplateView
from .forms import SubjectForm,CourseForm, ContentForm, ModuleForm, FileForm
from django.contrib import messages
from django.db import IntegrityError
from django.utils.text import slugify



# Create your views here.
def AddCourseView(request):
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        course_form = CourseForm(request.POST)
        content_form = ContentForm(request.POST)
        module_form = ModuleForm(request.POST)
        file_form = FileForm(request.POST)

        if subject_form.is_valid() and course_form.is_valid() and content_form.is_valid() and module_form.is_valid() and file_form.is_valid():
            try:
                subject=subject_form.save(commit=False)
                subject_title = subject.title#subject_form.cleaned_data['title']
                subject_slug = slugify(subject_title)
                subject, created = Subject.objects.get_or_create(title=subject_title, defaults={'slug': subject_slug})

                if not created:
                # Ensure the slug is unique by appending a number if necessary
                    unique_slug = subject_slug
                    num = 1
                    while Subject.objects.filter(slug=unique_slug).exists():
                        unique_slug = f'{subject_slug}-{num}'
                        num += 1
                    subject.slug = unique_slug
                    subject.save()

                
                course = course_form.save(commit=False)
                course.owner = request.user  # Set the owner to the current logged-in user
                course.subject = subject  # Assign the Subject instance to the Course
                
                # Save the course first to ensure it has a valid ID for other references
                course.save()

                # Create and save the module instance
                module = module_form.save(commit=False)
                module.course = course
                module.save()

                # Create and save the content instance
                content = content_form.save(commit=False)
                content.module = module 
                content.order = Content.objects.filter(module=module).count()
                content.save()

                # Create and save the itembase instance
                filebase = file_form.save(commit=False)
                # filebase.course = course
                filebase.owner= request.user
                filebase.save()

                return redirect('courses')
            except IntegrityError as e:
                if 'slug' in str(e):
                    messages.error(request, 'A course with the same slug already exists. Please use a different title.')
                else:
                    messages.error(request, 'An error occurred while saving the course.')
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {str(e)}')

    else:
        subject_form = SubjectForm()
        course_form = CourseForm()
        content_form = ContentForm()
        module_form = ModuleForm()
        file_form = FileForm()

    context = {
        'subject_form': subject_form,
        'course_form': course_form,
        'content_form': content_form,
        'module_form': module_form,
        'file_form': file_form,
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