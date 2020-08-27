from django.urls import path
from logs import views

app_name = 'logs'

urlpatterns = [

    path('get_name/',views.get_name, name='com'),
]
