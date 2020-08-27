from django.shortcuts import render
from django. http import HttpResponse
from django.template.loader import get_template
from .models import Photos

def top(request):
    topics = Photos.objects.all()
    return render(request,'image/image.html', {'topics': topics,})

def topic(request, id):
    id = Photos.objects.filter(id=id)
    return render(request,'image/carusel.html', {'id': id,})
