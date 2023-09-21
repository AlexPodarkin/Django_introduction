from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request -> index')
    return HttpResponse('<h2>Hello MyApp2 !</h2>')
