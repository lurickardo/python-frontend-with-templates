from django.shortcuts import render

def minha_pagina(request):
    return render(request, 'minha_pagina.html')
