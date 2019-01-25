from django.urls import path
from . import views
from .views import  LoginView, CreateStudentView

app_name = 'account'

urlpatterns = [
    path('register', CreateStudentView.as_view(), name ="signup"),
    path('register/student', CreateStudentView.as_view(), name="signup_student"),
    # path('signup', views.signup_view, name ="signup"),
    path('', LoginView.as_view(), name="login"),
    path('login', views.login_view, name ="login"),
    path('logout', views.logout_view, name ="logout"),
]
