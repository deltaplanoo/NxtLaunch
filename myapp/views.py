from django.shortcuts import render
from django.http import JsonResponse
import json
from .launch import *

def index(request):
    if not results:
        return render(request, 'error.html')
    
    context = {'json_data': results}

    return render(request, 'index.html', context)

def upcoming(request):
    if not results:
        return render(request, 'error.html')
    
    context = {'json_data': results}

    return render(request, 'upcoming.html', context)

def custom(request):
    if not results:
        return render(request, 'error.html')
    
    context = {'json_data': results}

    return render(request, 'custom.html', context)


def spacex(request):
    if not results:
        return render(request, 'error.html')
    
    context = {'json_data': results}

    return render(request, 'spacex.html', context)

def starship(request):
    if not results:
        return render(request, 'error.html')
    
    context = {'json_data': results}

    return render(request, 'starship.html', context)
