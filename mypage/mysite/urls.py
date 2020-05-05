from django.urls import path

from mysite import views
from mysite.views import other_page
from mysite.views import index
app_name = 'mysite'

urlpatterns = [
    path ('<str:page>/', other_page, name='other') ,
    path('',views.index, name='home'),
]
