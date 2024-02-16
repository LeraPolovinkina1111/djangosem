from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging
logger=logging.getLogger(__name__)
def index(request):
    logger.info('ничего')
    return HttpResponse('Hello world')


# Create your views here.

def game_1(request):
    answer = choice(['орел', 'решка'])
    logger.info(f'Ответ равен {answer}')
    return HttpResponse(answer)


def game_2(request):
    answer = randint(1, 6)
    logger.info(f'Ответ равен {answer}')
    return HttpResponse(answer)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f'Ответ равен {answer}')
    return HttpResponse(answer)
