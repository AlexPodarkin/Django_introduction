# from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('reqwest: Hello World')
    return HttpResponse('<h2>Hello World</h2>')


def heads_tails(request):
    num = randint(1, 2)
    result = 'Heads' if num == 2 else 'Tails'
    logger.debug(f'reqwest: heads_tails, answer: {result}')
    return HttpResponse(f'<h2>Бог рандома отвечает: {result} !')


def dice(request):
    num = randint(1, 6)
    logger.debug(f'reqwest: dice, answer: {num}')
    return HttpResponse(f'<h2>Кубик брошен: {num} !')


def random_num(request):
    num = randint(0, 100)
    logger.debug(f'reqwest: random_num, answer: {num}')
    return HttpResponse(f'<h2>Бог рандома отвечает: {num} !')
