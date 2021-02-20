from django.shortcuts import render
from django.http import HttpResponse

from .tasks import incluir_ligas


def get_ligas(request):
    incluir_ligas()
    return HttpResponse('times na fila para importacao')


# Create your views here.
