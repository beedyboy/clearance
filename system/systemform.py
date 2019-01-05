from django import forms
from . import models
from .models import FacultyData
#class FacultyCreationForm(forms.Form):
class FacultyCreationForm(forms.ModelForm):
    #faculty_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Faculty Name'}))
    class Meta:
        model = models.FacultyData
        fields = ['faculty_name']

        widgets = {
            'faculty_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Faculty Name'})
        }

class DepartmentCreationForm(forms.ModelForm):

    class Meta:
        model = models.DepartmentData
        fields = ['fid', 'dept_name']

        data = []
        #data.append((None, 'select one'))
        data.append(('20', "---Choose One---"))
        CHOICES = FacultyData.objects.all()

        for v in CHOICES:
            # fname = "%s -- $%d each" % (v.faculty_name, v.created_on)
            data.append((v.id, v.faculty_name))
    widgets = {
            'fid': forms.Select(attrs={'class': 'form-control'}),
            'dept_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'})
       }
