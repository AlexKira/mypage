from django.urls import path
from mysite import views
from django.urls import re_path
from mysite.views import contact
from mysite.views import home

app_name = 'mysite'

urlpatterns = [
    path('',views.home, name='home'),
    re_path('contact/',views.contact, name='contact'),

]
