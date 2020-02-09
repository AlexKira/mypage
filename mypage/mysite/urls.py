from django.urls import path
#mysite files
from . import views
app_name = 'mysite'

urlpatterns = [
	path('', views.index, name='index'),
	path('topics/<int:topic_id>/', views.topic, name='topic'),
]
