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
    fid = forms.ModelChoiceField(queryset=FacultyData.objects.all(), empty_label="Select One", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.DepartmentData
        fields = ['fid', 'dept_name']
        widgets = {

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
    sid = forms.ModelChoiceField(queryset=SessionData.objects.all(), empty_label="--Select Session--",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.SemesterData
        fields = ['sid', 'semester_name']

        widgets = {
            #'sid': forms.Select(attrs={'class': 'form-control'}),
           'semester_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Semester Name'}),

        }
