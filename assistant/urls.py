from django.urls import path

from . import views
from adtaa import views as adtaa_views

urlpatterns = [
	path('index', adtaa_views.index, name='index'),
    path('', views.scheduler, name='scheduler'),
    path('create_schedule', views.createSchedule, name='create_schedule'),
	path('scheduler/create_assignment', views.createAssignment, name='create_assignment'),
    path('update_assignment/<int:pk>/', views.updateAssignment, name='update_assignment'),
    path('delete_assignment/<int:pk>/', views.deleteAssignment, name='delete_assignment')
]
