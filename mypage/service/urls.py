from django.urls import path
from service import views
from django.urls import re_path
app_name = 'service'

urlpatterns = [
    path('',views.serv, name='service'),
]
