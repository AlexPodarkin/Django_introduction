from django.shortcuts import render


def index(request):
    return render(request, 'task_app/index.html')
