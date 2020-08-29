from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'manager/index.html', context)