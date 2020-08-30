from django.urls import path
from . import views
from course.models import Course

urlpatterns = [
    path('', views.manager_index, name='manager_index'),
    path('course/', views.course_list, name='course_list'),
    path('course/new', views.course_new, name='course_new'),
]