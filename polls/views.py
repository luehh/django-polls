from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo! Esta é a página inicial do aplicativo")

def produtos(request):
    return HttpResponse("Esta é a página dos produtos.")