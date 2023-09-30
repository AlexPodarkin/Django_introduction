from django.shortcuts import render
import logging
from . import forms
from . import models
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('reqwest index')
    return render(request, 'myapp4/index.html')


def user_form(request):
    """Простейшая реализация формы"""
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # работа БД
            logger.debug(f'result: {name=}, {email=}, {age=}.')

            # сообщения Flash
            messages.add_message(request, messages.SUCCESS, 'Успешно')
            # from django.contrib import messages
    else:
        form = forms.UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def user_form_2(request):
    if request.method == 'POST':
        form = forms.ManyFieldsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # work DB
            logger.info(f'get: {name=}, {email=}, {age=} \n all: {form.cleaned_data=}')
    else:
        form = forms.ManyFieldsForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = forms.ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # work DB
            logger.info(f'get: {name=}, {email=}, {age=} \n all: {form.cleaned_data=}')
    else:
        form = forms.ManyFieldsFormWidget()
    return render(request, 'myapp4/user_form.html', {'form': form})


def add_user(request):
    """Добавления пользователя"""
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # работа БД
            logger.debug(f'result: {name=}, {email=}, {age=}.')
            user = models.User(name=name, email=email, age=age)
            user.save()
            message = "Пользователь сохранен !"
            logger.debug(f'USER SAVE: {user}')
    else:
        form = forms.UserForm()
        message = "Заполните форму !"
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def show_users(request):
    users = models.User.objects.all()
    return render(request, 'myapp4/index.html', {'users': users})


def upload_image(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            # from django.core.files.storage import FileSystemStorage
            fs.save(image.name, image)
    else:
        form = forms.ImageForm()

    return render(request, 'myapp4/upload_image.html', {'form': form})


def choice_user(request):
    """Форма для вывода списком авторов"""
    if request.method == 'POST':
        form = forms.ChoiceUsers(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['user']
            # работа БД
            logger.debug(f'result: {recipient=}, {message=}.')

            # сообщения Flash
            messages.add_message(request, messages.SUCCESS, 'Успешно')
            # from django.contrib import messages
    else:
        form = forms.ChoiceUsers()
    return render(request, 'myapp4/user_form.html', {'form': form})
