from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login, logout

from .models import StudentProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import LoginForm, CreateStudentForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import CreateView, FormView
from django.utils.http import is_safe_url


from django.conf import settings
from django_tables2 import RequestConfig
from system.models import FacultyData, DepartmentData, SessionData, SemesterData, SettingsData

#import record tables

from system.tables import FacultyTable, DepartmentTable, SessionTable, SemesterTable
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.

class LoginView(FormView):

    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        user_id = form.cleaned_data.get('user_id')
        password = form.cleaned_data.get('password')
        user = authenticate(request, user_id=user_id, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_user_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


# class CreateStudentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
class CreateStudentView( CreateView):
    login_url = reverse_lazy('account:login')
    form_class = CreateStudentForm
    template_name = 'accounts/student/signup.html'
    success_message = 'New new user profile has been created'
    success_url = reverse_lazy('account:signup')

    def get_context_data(self, **kwargs):

        table = FacultyTable(FacultyData.objects.all())
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)

        context = super(CreateStudentView, self).get_context_data(**kwargs)
        context['app'] = settings.CONFIG
        context['faculty'] = table
        return context

    def form_valid(self, form):
        c = {'form': form, 'app': settings.CONFIG}
        user = form.save(commit=False)
        # Cleaned(normalized) data
        dept_name = form.cleaned_data['dept_name']
        semester = form.cleaned_data['semester']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        #set password
        user.set_password(password)
        user.user_type = 1
        user.save()
        # Create UserProfile model
        StudentProfile.objects.create(user=user, dept_name=dept_name, semester=semester, avatar = form.cleaned_data['avatar'])
        return super(CreateStudentView, self).form_valid(form)



def user_login(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #check
        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)

            if  request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/login.html", context)

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
# Create your views here.
def signup_view(request):
    #if request sent is post, then get all the data and put in a new instance of usercreationform
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #check if form is valid
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            #return HttpResponse('article page')
            return redirect('/')

    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #retrieve the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request, request.POST.get('next'))
            else:
            #login the user
                return redirect('/')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {"form": form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
