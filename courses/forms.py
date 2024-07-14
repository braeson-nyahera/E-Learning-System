from django import forms
from django.contrib.auth.models import User
from .models import Subject, Course, Module, Content, ItemBase, Video, File, Text, Image

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['title']

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['title','overview']

class ModuleForm(forms.ModelForm):
    class Meta:
        model=Module
        fields=['title','description','order']

class ContentForm(forms.ModelForm):
    class Meta:
        model=Content
        fields=['content_type','object_id',]

class ItembaseForm(forms.ModelForm):
    class Meta:
        model=ItemBase
        fields=['title']

if Content.content_type == 'video':  
    class FileForm(forms.ModelForm):
        class Meta:
            model=Video
            fields=['url']
elif Content.content_type == 'file': 
    class FileForm(forms.ModelForm):
        class Meta:
            model=File
            fields=['url']
elif Content.content_type == 'text': 
    class FileForm(forms.ModelForm):
        class Meta:
            model=Text
            fields=['url']
elif Content.content_type == 'image': 
    class FileForm(forms.ModelForm):
        class Meta:
            model=Image
            fields=['url']
else:
    class FileForm(forms.ModelForm):
        class Meta:
            model=Text
            fields=[]