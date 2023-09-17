from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('> Home page request <')
    return HttpResponse('<h2>Hello Alex</h2>')


def about(request):
    logger.debug('> Request about page <')
    # logger.error('work check')
    return HttpResponse('<h2>About us</h2>')
