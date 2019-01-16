from django.db import models
from system.models import FacultyData, DepartmentData, SessionData, SemesterData, SettingsData

# Create your models here.

class SchoolFees(models.Model):
    fid = models.ForeignKey(FacultyData, on_delete= models.SET_NULL, null=True)
    did = models.ForeignKey(DepartmentData, on_delete= models.SET_NULL, null=True)
    sid = models.ForeignKey(SessionData, on_delete= models.SET_NULL, null=True)
    amount = models.CharField(max_length=30)

    def __str__(self):
        return self.amount