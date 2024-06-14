from django.urls import path
from courses import views
from .views import SubjectListView, SubjectDetailView

urlpatterns = [
    path('', SubjectListView.as_view(), name='courses'),
    path('/<pk>', SubjectDetailView.as_view(), name='course_detail'),
]