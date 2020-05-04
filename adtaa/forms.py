from django.forms import ModelForm

from .models import Teacher, Course

class TeacherForm(ModelForm):
    class Meta:
            model = Teacher
            fields = ['last_name', 'first_name', 'email', 'class_load', 'areas']

class CourseForm(ModelForm):
    class Meta:
            model = Course
            fields = ['course_num', 'title', 'areas', 'meeting_day', 'meeting_time']
