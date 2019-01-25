# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from system.models import SemesterData, DepartmentData, SessionData
from django.http import HttpResponse

from .models import User, StudentProfile


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES,widget=forms.Select)
    # user_type = forms.Select(attrs={'class': 'form-control'})

    class Meta:
        model = User
        fields = ('user_id', 'first_name','last_name','user_type',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('user_id','first_name','last_name', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    user_id = forms.CharField(label="User Id", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter User Id'}))
    password = forms.CharField(widget=forms.PasswordInput)

 
class CreateStudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # Here we add the extra form fields that we will use to create another model object

    dept_name = forms.ModelChoiceField(queryset=DepartmentData.objects.all(), empty_label="Select One",
                                       widget=forms.Select(attrs={'class': 'form-control'}), label="Select One")
    sid = forms.ModelChoiceField(queryset = SessionData.objects.all(), empty_label = "--Select Session--",
                                 widget = forms.Select(attrs = {'class': 'form-control'}))
    semester = forms.ModelChoiceField(queryset=SemesterData.objects.all(), empty_label="Select Session First",
                                      widget=forms.Select(attrs={'class': 'form-control'}), label="Select One")
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'user_id', 'first_name', 'last_name',
        ]
        widgets = {

            'user_id': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Matric Num or Student Id '}),
            'first_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Last Name'}),

        }

    def __init__(self, *args, **kwargs):
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields['semester'].queryset = SemesterData.objects.none()

       # Get did queryset for the selected fid
        if 'sid' in self.data:
            try:
                fd = int(self.data.get('sid'))
                self.fields['semester'].queryset = SemesterData.objects.filter(sid_id=fd).order_by('id')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['semester'].queryset = self.instance.sid.semesterdata_set.order_by('id')


