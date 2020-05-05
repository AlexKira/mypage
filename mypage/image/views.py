from django.shortcuts import render
from django. http import HttpResponse
from django.template.loader import get_template
from django.views.generic.list import ListView
from image.models import NewsWork

class Power(ListView):
    context_object_name = 'NewsWork'
    template_name ='image/news.html'

    def get_queryset(self):
        return NewsWork.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['-date_added'] = NewsWork.objects.all()
        return context
