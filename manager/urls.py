from django.urls import path
from . import views
from course.models import Course

urlpatterns = [
    path('', views.manager_index, name='manager_index'),
    # Course Model urls
    path('course/', views.course_list, name='course_list'),
    path('course/new', views.course_new, name='course_new'),
    path('course/edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),
]