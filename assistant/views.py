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

def createAssignment(request):
	form = ScheduleForm()
	if request.method == 'POST':
		form = ScheduleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('scheduler')
	context = {'form':form,}
	if request.user.groups.filter(name="Admin").exists() or request.user.groups.filter(name="Scheduler").exists() or request.user.is_staff:
		return render(request, 'assistant/schedule_form.html', context)
	else:
		return redirect("/")

def updateAssignment(request, pk):
	schedule = Schedule.objects.get(id=pk)
	form = ScheduleForm(instance=schedule)

	if request.method == 'POST':
		form = ScheduleForm(request.POST, instance=schedule)
		if form.is_valid():
			form.save()
			return redirect('scheduler')

	context = {'form':form}
	if request.user.groups.filter(name="Admin").exists() or request.user.groups.filter(name="Scheduler").exists() or request.user.is_staff:
		return render(request, 'assistant/schedule_form.html', context)
	else:
		return redirect("/")

def deleteAssignment(request, pk):
	schedule = Schedule.objects.get(id=pk)
	if request.method == 'POST':
		schedule.delete()
		return redirect('scheduler')

	context = {'schedule':schedule}
	if request.user.groups.filter(name="Admin").exists() or request.user.groups.filter(name="Scheduler").exists() or request.user.is_staff:
		return render(request, 'assistant/delete_schedule.html', context)
	else:
		return redirect("/")