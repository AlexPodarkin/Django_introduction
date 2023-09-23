from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from . import models
import logging

logger = logging.getLogger(__name__)
my_dict = dict()


def dice(reqwest):
    rand = choice(['heads', 'tails'])
    result = models.RememberDice(position=rand)
    result.save()
    logger.debug(f'Монета брошена: {result}')
    statistic = models.RememberDice.stat(my_dict, result.pk, result.position)
    return HttpResponse(f'<h2>Монета брошена: {result}</h2>'
                        f'<h3>Статистика  по n последним броскам монеты: {statistic}</h3>')
