from django import forms
from django.contrib.auth.models import User
from .models import Subject, Course, Module, Content, ItemBase

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
        fields=['content_type','object_id']

class ItembaseForm(forms.ModelForm):
    class Meta:
        model=ItemBase
        fields=['title']