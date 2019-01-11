from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from model_utils import Choices

# Create your models here.

class FacultyData(models.Model):
    faculty_name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.faculty_name


class DepartmentData(models.Model):
    fid = models.ForeignKey(FacultyData, on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dept_name

class SessionData(models.Model):
    session_name = models.CharField(max_length=15)

    def __str__(self):
        return self.session_name

# class SemesterData(models.Model):
#     YESNOCHOICE = (
#         ('Y', 'Yes'),
#         ('N', 'No'),
#     )
#     sid = models.ForeignKey(SessionData,on_delete=models.CASCADE)
#     semester_name = models.CharField(max_length=50)
#     status = models.CharField(max_length=3, choices=YESNOCHOICE, blank=True, default=YESNOCHOICE[1][0])

class SemesterData(models.Model):
    sid = models.ForeignKey(SessionData, on_delete=models.CASCADE)
    semester_name = models.CharField(max_length=50)
    def __str__(self):
            return self.semester_name

    def current(self):
        st = SettingsData.objects.get(id=1)
        if self.id == st.current_id:
            return "Current Session-Semester"
        else:
            return format_html('<a href="{}">{}</a>', reverse('system:current_session_semester', args=[self.id] ),   'Set Current')
            #return format_html('<a href="{}">{}</a>',  self.id, 'Set Current')
           # return format_html('<a href="' + str(self.id) + '/view/' + ' ">Set</a>')


class SettingsData(models.Model):
    current = models.ForeignKey(SemesterData, on_delete=models.SET_NULL, null=True)

    # YESNOCHOICE = Choices(
    #     (0, 'yes', 'Yes'),
    #     (1, 'no', 'No'),
    # )
    #
    # status = models.IntegerField(choices=YESNOCHOICE,  default=YESNOCHOICE.no)