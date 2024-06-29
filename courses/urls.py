from django.urls import path
from courses import views
from .views import CourseListView, CourseDetailView, ModuleDetailView, SearchView

urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('/<pk>', CourseDetailView.as_view(), name='course_detail'),
    path('/module/<pk>', ModuleDetailView.as_view(), name='module_detail'),
    path('search',views.SearchView,name='search'),
]