from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

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