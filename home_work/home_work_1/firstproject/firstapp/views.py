from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request: "index"')
    html = '<h1>Main</h1>' \
           '<h2>My first project !<h1>' \
           '<h4><a href="http://127.0.0.1:8000/about/">clik to Information about us</a></h4>'
    return HttpResponse(html)


def about(request):
    logger.debug('request: "about"')
    html = '<h1>Information about us:</h1>' \
           '<h2>Alex PodarkiN</h2>' \
           '<h3>I`m learning Django</h3>' \
           '<h4><a href="http://127.0.0.1:8000/">clik to main</a></h4>'
    return HttpResponse(html)
