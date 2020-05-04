from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    #path('baker', views.TeacherView, name='TeacherView'),
    path('create_teacher', views.createTeacher, name='create_teacher'),
    path('update_teacher/<str:pk>/', views.updateTeacher, name='update_teacher'),
    path('delete_teacher/<str:pk>/', views.deleteTeacher, name='delete_teacher'),
    path('create_course', views.createCourse, name='create_course'),
    path('update_course/<str:pk>/', views.updateCourse, name='update_course'),
    path('delete_course/<str:pk>/', views.deleteCourse, name='delete_course')
]
