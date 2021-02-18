from django.shortcuts import render
from django.http import HttpResponse

from .tasks import incluir_times


def get_times(request):
    incluir_times()
    return HttpResponse('times na fila para importacao')
