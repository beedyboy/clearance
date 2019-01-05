from django.shortcuts import render, redirect, get_object_or_404
from .systemform import FacultyCreationForm, DepartmentCreationForm
from django.utils import timezone
from django.conf import settings
from .models import FacultyData
from django.contrib import messages
from django_tables2 import RequestConfig
from django.http import HttpResponse
#import django_filters
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
    app = settings.CONFIG
    table = FacultyTable(FacultyData.objects.all())
    RequestConfig(request, paginate={'per_page': 10 }).configure(table)
    context = {"form": FacultyCreationForm, 'faculty': table, 'app': app}
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

def view_faculty(request):
    app = settings.CONFIG
    data = FacultyData.objects.all()
    return render(request, 'faculty/view.html', {'faculty': data, 'app': app})

def fac_link_edit(request, id):
    app = settings.CONFIG
    #get faculty by id
    post = get_object_or_404(FacultyData, pk=id)
    return HttpResponse(post)
    form = FacultyCreationForm(initial=post)
    table = FacultyTable(FacultyData.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    context = {"form": form, 'faculty': table, 'app': app}
    return render(request, 'faculty/editfaculty.html', context)


def fac_link_view(request, id):

    return HttpResponse(id)


def create_dept(request):
    app = settings.CONFIG
    context = {}
    table = FacultyTable(FacultyData.objects.all())
    RequestConfig(request, paginate={'per_page': 10 }).configure(table)
    context = {"form": DepartmentCreationForm, 'faculty': table, 'app': app}

    return render(request, 'dept/create.html', context)
