from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeesCreationForm
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from .tables import FeesTable
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.core import serializers
from system.models import FacultyData, DepartmentData, SessionData, SemesterData, SettingsData
from .models import SchoolFees

# Create your views here.

def create_fee(request):
    app = settings.CONFIG
    table = FeesTable(SchoolFees.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    context = {"form": FeesCreationForm, "fees":table, 'app': app}
    return render(request, 'bursary.html', context)

def get_department(request):

    fid = request.GET.get('fid', None)

    datas = {
        'is_taken': DepartmentData.objects.filter(fid_id=fid)
    }
    department = list(DepartmentData.objects.filter(fid_id=fid).values())
    data = dict()
    data['department'] = department
    return JsonResponse(data)

def save_fee(request):
    app = settings.CONFIG
    table = FeesTable(SchoolFees.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    form = FeesCreationForm(request.POST)
    # ex = request.POST.get('did', False)
    # return HttpResponse(ex)
    context = {"form": FeesCreationForm, "fees":table, 'app': app}
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Fees added successfully")
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    return redirect('bursary:create_fee')

def edit_fee(request, pk):
    app = settings.CONFIG
    post = get_object_or_404(SchoolFees, pk=pk)
    if request.method == 'POST':
        form = FeesCreationForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.WARNING, "Fees record updated successfully")
            return redirect('bursary:create_fee')

    else:
        # bring edit form out
        form = FeesCreationForm(instance=post)
        table = FeesTable(SchoolFees.objects.all())
        RequestConfig(request, paginate={'per_page': 10}).configure(table)
        context = {"form": form, "fees": table, 'app': app}


    return render(request, 'editfee.html', context)

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = FeesCreationForm