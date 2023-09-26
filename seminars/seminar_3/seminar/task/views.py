from random import randint

from django.shortcuts import render


def index(request):
    context = {
        'name': 'quest',
        'page': 'index',
    }
    return render(request, 'task/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'description': 'Welcome',
    }
    return render(request, 'task/about.html', context)


def dice(request, count):
    res_list = list()
    for i in range(count):
        res_list.append(randint(1, 6))
    context = {
        'results': res_list,
        'len': len(res_list),
        'title': 'Dice',
    }
    return render(request, 'task/dice.html', context)
