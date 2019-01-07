from django import forms
from . import models
from .models import FacultyData,SessionData
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

        #data.append( "---Choose One---")
        CHOICES = FacultyData.objects.all()

        for v in CHOICES:
            # fname = "%s -- $%d each" % (v.faculty_name, v.created_on)
            data.append((v.id, v.faculty_name))
        # 
        #fid = forms.ModelChoiceField(queryset=FacultyData.objects.all(), label="Select One", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
        #fid= forms.ModelChoiceField(queryset=FacultyData.objects.all(), empty_label="Select One", to_field_name=None)
        widgets = {
            'fid': forms.Select(attrs={'class': 'form-control'}),
           'dept_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'})
       }

class SessionCreationForm(forms.ModelForm):
     class Meta:
        model = models.SessionData
        fields = ['session_name']

        widgets = {
            'session_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Session year'})
        }

class SemesterCreationForm(forms.ModelForm):

    class Meta:
        model = models.SemesterData
        fields = ['sid', 'semester_name']

        data = []
        CHOICES = SessionData.objects.all()

        for v in CHOICES:

            data.append((v.id, v.session_name))

        widgets = {
            'sid': forms.Select(attrs={'class': 'form-control'}),
           'semester_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Semester Name'})
        }
