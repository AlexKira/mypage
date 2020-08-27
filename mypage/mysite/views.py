from django.shortcuts import render
from mysite.models import Contact

def home(request) :
	contact = Contact.objects.all()
	return render(request, 'mysite/home.html', {'contact':contact})

def contact(request) :
	con = Contact.objects.all()
	return render(request, 'mysite/contact.html', {'con':con})
