from django.urls import path,include
from . models import Photos
from image import views
from image.views import top
from image.views import topic
from django.views.generic import ListView
from django.urls import re_path
app_name = 'image'

urlpatterns = [

	re_path('^$', views.top, name='index'),
	path('topics/<id>/', views.topic, name = 'index'),

]
