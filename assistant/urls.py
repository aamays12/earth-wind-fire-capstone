from django.urls import path

from . import views

urlpatterns = [
    path('', views.scheduler, name='scheduler'),
    path('create_schedule', views.createSchedule, name='create_schedule'),
	path('test', views.helloWorld, name='test')
]
