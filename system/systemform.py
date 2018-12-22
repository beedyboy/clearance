from django import forms

class FacultyCreationForm(forms.Form):
    #faculty_name = forms.CharField(max_length=30)
    faculty_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Faculty Name'}))
