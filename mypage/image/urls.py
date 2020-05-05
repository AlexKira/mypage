from django.urls import path,include
from image import views
from django.views.generic.list import ListView
from image.views import Power
from django.urls import re_path
app_name = 'image'

urlpatterns = [
	re_path('^$', Power.as_view(), name='index'),
]
