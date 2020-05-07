from django.urls import path

from . import views
from adtaa import views as adtaa_views

urlpatterns = [
	path('index', adtaa_views.index, name='index'),
    path('', views.scheduler, name='scheduler'),
    path('create_schedule', views.createSchedule, name='create_schedule')
]
