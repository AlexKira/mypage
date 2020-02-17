from django.shortcuts import render
from .models import Topic

def index(request):
	topics = Topic.objects.order_by('-date_added')
	context = {
		'topics': topics,
	}
	return render(request,
		'mysite/index.html', context)

def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {
		'topic': topic,
		'entries': entries,
	}
	return render(request,
		'mysite/topic.html', context)
