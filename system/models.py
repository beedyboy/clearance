from django.db import models
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

class SemesterData(models.Model):
    sid = models.ForeignKey(SessionData,on_delete=models.CASCADE)
    semester_name = models.CharField(max_length=50)

    def __str__(self):
        return self.semester_name