from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from . import models
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request: index')
    return HttpResponse('<h2>Task 2(seminar3), работаем через консоль, загляните в файл view</h2>')

# Добавить продукты:
# python .\manage.py fake_product 50(количество фейковых продуктов)
