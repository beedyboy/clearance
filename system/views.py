from django.shortcuts import render, redirect
from .systemform import FacultyCreationForm
from django.utils import timezone
from django import  forms
from .models import FacultyData
from django.contrib import messages
from django_tables2 import RequestConfig
from .tables import FacultyTable
# Create your views here.


def create_faculty(request):
    # form = FacultyCreationForm(request.POST)
    # if form.is_valid():
    #     if FacultyData.objects.filter(faculty_name=request.POST['faculty_name']).exists():
    #         return HttpResponse(" Data already exist")
    #     else:
    #         register = FacultyData(faculty_name=form.cleaned_data['faculty_name'])
    #         register.created_on = timezone.now()
    #         register.save()
    # return redirect('system:fac_create')
    table = FacultyTable(FacultyData.objects.all())
    RequestConfig(request, paginate={'per_page': 10 }).configure(table)
    context = {"form": FacultyCreationForm, 'faculty': table}
    return render(request, 'faculty/create.html', context)

def add_faculty(request):

    form = FacultyCreationForm(request.POST)
    if form.is_valid():
        if FacultyData.objects.filter(faculty_name = request.POST['faculty_name']).exists():
           messages.add_message(request, messages.WARNING, "Faculty already exist")
        else:
            register = FacultyData(faculty_name = form.cleaned_data['faculty_name'])
            register.created_on = timezone.now()
            register.save()
            messages.add_message(request, messages.SUCCESS, "Faculty added successfully")
    return redirect('system:fac_create')

def create_dept(request):
    context = {}
    faculty_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={ 'class': 'uk-input'}))

    dept_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={ 'class': 'uk-select', 'placeholder':'Department Name'}))


    return render(request, 'dept/create.html', context)
