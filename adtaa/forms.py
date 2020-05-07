from django.forms import ModelForm

from .models import Teacher, Course, Schedule

class TeacherForm(ModelForm):
    class Meta:
            model = Teacher
            fields = ['last_name', 'first_name', 'email', 'class_load', 'areas']

class CourseForm(ModelForm):
    class Meta:
            model = Course
            fields = ['course_num', 'title', 'areas', 'meeting_day', 'meeting_time']

class ScheduleForm(ModelForm):
    class Meta:
            model = Schedule
            fields = ['course_num', 'title', 'last_name', 'first_name', 'meeting_day', 'meeting_time']