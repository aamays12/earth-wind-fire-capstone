from adtaa.models import Teacher, Course, Area, Schedule
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        Schedule.objects.all().delete()
        teach_list = Teacher.objects.all()
        course_list = Course.objects.all()
        schedule_list = Schedule.objects.all()
        #schedule_list = Schedule.objects.all()
        t_count = Teacher.objects.count()
        c_count = Course.objects.count()
        a_count = Area.objects.count()

        const_teach_list = teach_list
        no_teach_list = Schedule()
        load_list = []



        for i in range(t_count):
            load_list.append(teach_list[i].class_load)

        for p in range(c_count):
            #---------------------------------------------------------------------------
            load = 0
            loc = 0
            teach_per_area = []
            temp_teach_list =[]
            for i in range(1, (a_count+1)):
                temp_teach_list = teach_list.filter(areas=i)
                if (not temp_teach_list):
                    load = (t_count+1+c_count)
                for j in range(len(temp_teach_list)):
                    loc = list(const_teach_list).index(temp_teach_list[j])
                    load += load_list[loc]
                teach_per_area.append(load)
                load = 0
                temp_teach_list = []

            #print(teach_per_area)

            #---------------------------------------------------------------------------
            course_per_area = []
            temp_course_list = []
            for i in range(1, (a_count+1)):
                temp_course_list = course_list.filter(areas=i)
                for j in range(len(temp_course_list)):
                    load += 1
                if (len(temp_course_list) == 0):
                    load = -(c_count+1+t_count)
                course_per_area.append(load)
                load = 0
                temp_course_list = []
            #print(course_per_area)

            #---------------------------------------------------------------------------
            differnce_list = [];
            for i in range(a_count):
                differnce_list.append(teach_per_area[i] - course_per_area[i])

            #print(differnce_list)
            area_priority = ((differnce_list.index(min(differnce_list))) + 1)
            #print(area_priority)

            #---------------------------------------------------------------------------
            temp_course_count = []
            temp_course_count = list(course_list.filter(areas=area_priority))

            assign_course = [];
            x = 1
            while(not assign_course):
                if len(temp_course_count) == 0:
                    print("error")
                    break
                for j in range(len(temp_course_count)):
                        if temp_course_count[j].areas.count() == x:
                            assign_course = temp_course_count[j]
                            break
                x += 1
            #print(assign_course)

            #---------------------------------------------------------------------------
            temp_teach_count = []
            assign_teacher = []
            conflict_list =[]
            x = 1

            for i in range(len(schedule_list)):
                if (schedule_list[i].meeting_day==assign_course.meeting_day)and(schedule_list[i].meeting_time==assign_course.meeting_time):
                    conflict_list = schedule_list[i]

            if (conflict_list and const_teach_list):
                for i in range(len(conflict_list)):
                    temp_teach_count = teach_list.filter(areas=area_priority).exclude(last_name=conflict_list[i].last_name)
            else:
                temp_teach_count = teach_list.filter(areas=area_priority)

            no_teacher = True
            while(not assign_teacher):
                if len(temp_teach_count) == 0:
                    no_teach_list = Schedule(
                    course_num = assign_course.course_num,
                    title = assign_course.title,
                    meeting_day = assign_course.meeting_day,
                    meeting_time = assign_course.meeting_time,
                    last_name = 'UNASSIGNED',
                    first_name = 'UNASSIGNED')
                    no_teach_list.save()
                    no_teacher = False
                     # write method to print out no teacher for this course
                    break
                for j in range(len(temp_teach_count)):
                        if temp_teach_count[j].areas.count() == x:
                            assign_teacher = temp_teach_count[j]
                            loc = list(const_teach_list).index(temp_teach_count[j])
                            load_list[loc] -= 1
                            break
                x += 1
            #    print(assign_teacher)

            if (assign_course):
                course_list = course_list.exclude(course_num=assign_course.course_num)

            if (assign_teacher):
                if (load_list[loc] <= 0):
                    teach_list = teach_list.exclude(last_name=assign_teacher.last_name)

            #---------------------------------------------------------------------------
            if (no_teacher):
                create_schedule_list = Schedule(
                course_num = assign_course.course_num,
                title = assign_course.title,
                meeting_day = assign_course.meeting_day,
                meeting_time = assign_course.meeting_time,
                last_name = assign_teacher.last_name,
                first_name = assign_teacher.first_name)
                create_schedule_list.save()

            #return 1
