from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_1to4(value):
    if value < 0 or value > 4:
        raise ValidationError(
            _('%(value)s is not between 0 and 4 inclusive'),
            params={'value': value},
        )

class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    last_name = models.CharField(max_length=200, primary_key=True)
    first_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, blank=True)
    class_load = models.IntegerField(validators=[validate_1to4])
    areas = models.ManyToManyField('Area', verbose_name='teacher areas')

    def __str__(self):
        return self.last_name

    def get_area_values(self):
        ret = ''
        print(self.areas.all())
        # use models.ManyToMany field's all() method
        for area in self.areas.all():
            ret = ret + area.name + ', '
        # remove the last ',' and return the value.
        return ret[:-2]


class Course(models.Model):
    course_num = models.CharField(max_length=4, primary_key=True)
    title = models.CharField(max_length=200)
    areas = models.ManyToManyField(Area,  verbose_name='course areas')
    MONDAY = 'MW'
    TUESDAY = 'TH'
    MEET_DAY_CHOICES = [
        (MONDAY, 'Monday Wednesday'),
        (TUESDAY, 'Tuesday Thursday'),
    ]
    AM800= '8:00AM-9:15AM'
    AM925= '9:25AM-10:40AM'
    AM1050= '10:50AM-12:05PM'
    PM1215= '12:15PM-1:30PM'
    PM140= '1:40PM-2:55PM'
    PM305= '3:05PM-4:20PM'
    PM430= '4:30PM-5:45PM'
    PM555= '5:55PM-7:10PM'
    MEET_TIME_CHOICES = [
        (AM800, '8:00AM-9:15AM'),
        (AM925, '9:25AM-10:40AM'),
        (AM1050, '10:50AM-12:05PM'),
        (PM1215, '12:15PM-1:30PM'),
        (PM140, '1:40PM-2:55PM'),
        (PM305, '3:05PM-4:20PM'),
        (PM430, '4:30PM-5:45PM'),
        (PM555, '5:55PM-7:10PM'),
    ]
    meeting_day = models.CharField(max_length=2, choices=MEET_DAY_CHOICES)
    meeting_time = models.CharField(max_length=15, choices=MEET_TIME_CHOICES)

    def __str__(self):
        return self.title

    def get_area_values(self):
        ret = ''
        print(self.areas.all())
        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for area in self.areas.all():
            ret = ret + area.name + ', '
        # remove the last ',' and return the value.
        return ret[:-2]


class Schedule(models.Model):
    course_num = models.CharField(max_length=4)
    title = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    MONDAY = 'MW'
    TUESDAY = 'TH'
    MEET_DAY_CHOICES = [
        (MONDAY, 'Monday Wednesday'),
        (TUESDAY, 'Tuesday Thursday'),
    ]
    AM800= '8:00AM-9:15AM'
    AM925= '9:25AM-10:40AM'
    AM1050= '10:50AM-12:05PM'
    PM1215= '12:15PM-1:30PM'
    PM140= '1:40PM-2:55PM'
    PM305= '3:05PM-4:20PM'
    PM430= '4:30PM-5:45PM'
    PM555= '5:55PM-7:10PM'
    MEET_TIME_CHOICES = [
        (AM800, '8:00AM-9:15AM'),
        (AM925, '9:25AM-10:40AM'),
        (AM1050, '10:50AM-12:05PM'),
        (PM1215, '12:15PM-1:30PM'),
        (PM140, '1:40PM-2:55PM'),
        (PM305, '3:05PM-4:20PM'),
        (PM430, '4:30PM-5:45PM'),
        (PM555, '5:55PM-7:10PM'),
    ]
    meeting_day = models.CharField(max_length=2, choices=MEET_DAY_CHOICES)
    meeting_time = models.CharField(max_length=15, choices=MEET_TIME_CHOICES)
