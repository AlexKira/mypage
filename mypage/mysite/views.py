from django.shortcuts import render
from .models import Topic

def index(request):

    return render(request,'mysite/index.html')

def topic(request, topic_id):

    return render(request,'mysite/topic.html')
