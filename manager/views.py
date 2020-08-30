from django.shortcuts import render, redirect
from course.models import Course
from course.forms import CourseForm

def manager_index(request):
    context = {}
    return render(request, 'manager/index.html', context)

def course_list(request):
    context = {}
    return render(request, 'manager/course/list.html', context)

def course_new(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid:
            try:
                form.save()
                return redirect('course_list')
            except:
                return render(request, 'manager/course/new.html', context)
        #     return redirect('course_list')
    else: 
        context = {
            'form': form
        }
        return render(request, 'manager/course/new.html', context)