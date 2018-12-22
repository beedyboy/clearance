from django.db import models
# Create your models here.

class FacultyData(models.Model):
    faculty_name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.faculty_name



'''class RegistrationData(models.Model):
    #fid = models.ForeignKey()
    dept_name = models.CharField(max_length=30)
    #author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

'''