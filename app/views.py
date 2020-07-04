from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def orcamento(request):
    return render(request, 'orcamento.html')

def contato(request):
    return render(request, 'contato.html')
