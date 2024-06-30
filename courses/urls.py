from django.urls import path
from .views import CourseListView, CourseDetailView, ModuleDetailView, SearchView, AddCourseView

urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('module/<int:pk>/', ModuleDetailView.as_view(), name='module_detail'),
    path('search/', SearchView, name='search'),
    path('/add_course/', AddCourseView, name='add_course'),
]
