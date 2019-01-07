from django.shortcuts import render, redirect, get_object_or_404
from .systemform import FacultyCreationForm, DepartmentCreationForm, SessionCreationForm,SemesterCreationForm
from django.utils import timezone
from django.conf import settings
from .models import FacultyData, DepartmentData, SessionData, SemesterData
from django.contrib import messages
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
from django.http import HttpResponse
#import django_filters
from .tables import FacultyTable, DepartmentTable, SessionTable, SemesterTable
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

def fac_link_edit(request, pk):

    #return HttpResponse(pk)
    app = settings.CONFIG
    #get faculty by id
    post = get_object_or_404(FacultyData, pk=pk)

    if request.method == 'POST':
        #then form is trying to save
        form = FacultyCreationForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.WARNING, "Faculty record updated successfully")
        return redirect('system:fac_view')

    else:
        #bring edit form out
        form = FacultyCreationForm(instance=post)
        table = FacultyTable(FacultyData.objects.all())
        RequestConfig(request, paginate={'per_page': 10}).configure(table)

        context = {"form": form, 'faculty': table, 'app': app}
    return render(request, 'faculty/editfaculty.html', context)


def fac_link_view(request, id):
    app = settings.CONFIG
    context = []
    #get record
    faculty = FacultyData.objects.get(id=id)

    #get total department under faculty
    dept = DepartmentData.objects.filter(fid=id)

    paginator = Paginator(dept, 1)

    page = request.GET.get('page')
    department = paginator.get_page(page)


    context = {'faculty': faculty, 'dept': dept, 'department': department, 'app': app}

    return render(request, 'faculty/viewfaculty.html', context)


def create_dept(request):
    app = settings.CONFIG
    context = {}
    table = DepartmentTable(DepartmentData.objects.all())
    RequestConfig(request, paginate={'per_page': 10 }).configure(table)
    context = {"form": DepartmentCreationForm, 'faculty': table, 'app': app}

    return render(request, 'dept/create.html', context)

def add_dept(request):

    form = DepartmentCreationForm(request.POST)
    if form.is_valid():
        if DepartmentData.objects.filter(fid = request.POST['fid'], dept_name = request.POST['dept_name']).exists():
           messages.add_message(request, messages.WARNING, "Department already exist under this faculty")
        else:
            register = DepartmentData(fid = form.cleaned_data['fid'],dept_name = form.cleaned_data['dept_name'])
            register.created_on = timezone.now()
            register.save()
            messages.add_message(request, messages.SUCCESS, "Department added successfully")
    return redirect('system:dept_create')


def create_session(request):
    app = settings.CONFIG
    context = {}
    table = SessionTable(SessionData.objects.all())
    RequestConfig(request, paginate={'per_page': 10 }).configure(table)
    context = {"form": SessionCreationForm, 'session': table, 'app': app}

    return render(request, 'session/session.html', context)

def add_session(request):
    form = SessionCreationForm(request.POST)
    if form.is_valid():
      if SessionData.objects.filter(session_name =request.POST['session_name']).exists():
          messages.add_message(request,messages.WARNING, "This session year already exist")
      else:
              register = SessionData(session_name=form.cleaned_data['session_name'])
              register.save()
              messages.add_message(request, messages.SUCCESS, "New session year has been added successfully")
      return redirect('system:session_create')

def session_edit(request, pk):
    app = settings.CONFIG
    post = get_object_or_404(SessionData, pk=pk)

    if request.method == 'POST':
        #then form is trying to save
        form = SessionCreationForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.WARNING, "Session record updated successfully")
        return redirect('system:session_create')

    else:
        #bring edit form out
        form = SessionCreationForm(instance=post)
        table = SessionTable(SessionData.objects.all())
        RequestConfig(request, paginate={'per_page': 10}).configure(table)

        context = {"form": form, 'session': table, 'app': app}
    return render(request, 'session/editsession.html', context)


def create_semester(request):
        app = settings.CONFIG
        context = {}
        table = SemesterTable(SemesterData.objects.all())
        RequestConfig(request, paginate={'per_page': 10}).configure(table)
        context = {"form": SemesterCreationForm, 'semester': table, 'app': app}

        return render(request, 'semester/semester.html', context)

def add_semester(request):

    form = SemesterCreationForm(request.POST)
    if form.is_valid():
        if SemesterData.objects.filter(sid = request.POST['sid'], semester_name = request.POST['semester_name']).exists():
           messages.add_message(request, messages.WARNING, "Semester already exist under this session")
        else:
            register = SemesterData(sid = form.cleaned_data['sid'],semester_name = form.cleaned_data['semester_name'])
            register.save()
            messages.add_message(request, messages.SUCCESS, "Semester added successfully")
    return redirect('system:create_semester ')

