from django.urls import path
from home import views
from .views import CourseListView

urlpatterns = [
    path('', views.landing, name='landing_page'),
    path('base/',views.base,name='base'),
    path('home/',CourseListView.as_view(),name='home'),
]