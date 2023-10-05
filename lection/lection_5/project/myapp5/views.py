from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp5/index.html')

# Настройка языка
# LANGUAGE_CODE = 'ru-ru' (файл settings.py)

# Создание суперпользователя
# python manage.py createsuperuser
# (admin@mail.ru)

# Сброс пароля
# python manage.py changepassword <username>

#  Внимание! Для выхода из административной панели можно использовать
# адрес http://127.0.0.1:8000/admin/logout/ или нажать ссылку в правом верхнем углу страницы.

# user
# %qwerty12345
# admin


