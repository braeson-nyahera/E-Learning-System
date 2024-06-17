from django.urls import path
from courses import views
from .views import SubjectListView, SubjectDetailView, ModuleDetailView

urlpatterns = [
    path('', SubjectListView.as_view(), name='courses'),
    path('/<pk>', SubjectDetailView.as_view(), name='course_detail'),
    path('/module/<pk>', ModuleDetailView.as_view(), name='module_detail'),
]