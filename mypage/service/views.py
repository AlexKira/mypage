from django.shortcuts import render
from service.models import Service

# Create your views here.

def serv(request):
	servic = Service.objects.all()
	service = Service.objects.all()
	context = {
	'servic': servic,
	'service': service,
	}
	return render(request,'service/service.html', context)
