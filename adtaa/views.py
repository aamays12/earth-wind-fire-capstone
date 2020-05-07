from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.views.generic.edit import FormView

from .forms import TeacherForm, CourseForm
from .models import Teacher, Course

def index(request):
    teacher_list = Teacher.objects.order_by('-last_name')
    course_list = Course.objects.order_by('-course_num')

    context = {
        'teacher_list' : teacher_list,
        'course_list' : course_list,
    }
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/index.html', context)
    else:
        return redirect("/")
    

def createTeacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/teacher_form.html', context)
    else:
        return redirect("/")

def updateTeacher(request, pk):

    teacher = Teacher.objects.get(last_name=pk)
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/teacher_form.html', context)
    else:
        return redirect("/")

def deleteTeacher(request, pk):
    teacher = Teacher.objects.get(last_name=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('index')

    context = {'teacher':teacher}
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/delete_teacher.html', context)
    else:
        return redirect("/")

def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form,}
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/course_form.html', context)
    else:
        return redirect("/")
    

def updateCourse(request, pk):

    course = Course.objects.get(course_num=pk)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/course_form.html', context)
    else:
        return redirect("/")

def deleteCourse(request, pk):
    course = Course.objects.get(course_num=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('index')

    context = {'course':course}
    if request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
        return render(request, 'adtaa/delete_course.html', context)
    else:
        return redirect("/")


















#class TeacherView(FormView):
#    template_name = 'index.html'
#    form_class = TeacherForm
#    success_url = '/thanks/'
#
#    def form_valid(self, form):
#        # This method is called when valid form data has been POSTed.
#        # It should return an HttpResponse.
#        return HttpResponseRedirect('/thanks/')

# Create your views here.
