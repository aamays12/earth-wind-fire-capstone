from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.views.generic.edit import FormView

from adtaa.forms import TeacherForm, CourseForm, ScheduleForm
from adtaa.models import Teacher, Course, Schedule
from django.core import management
from django.core.management import call_command

def scheduler(request):
	schedule_list = Schedule.objects.order_by('meeting_day', 'meeting_time', 'course_num')

	context = {
		'schedule_list' : schedule_list,
	}
	if request.user.groups.filter(name="Admin").exists() or request.user.groups.filter(name="Scheduler").exists() or request.user.is_staff:
		return render(request, 'assistant/scheduler.html', context)
	else:
		return redirect("/")

def createSchedule(request):
	if request.method == 'POST':
		call_command('scheduler')
		return redirect('scheduler')
	if request.user.groups.filter(name="Admin").exists() or request.user.groups.filter(name="Scheduler").exists() or request.user.is_staff:
		return render(request, 'assistant/create_schedule.html')
	else:
		return redirect("/")