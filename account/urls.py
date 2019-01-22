from django.urls import path
from . import views
from .views import LoginView, RegisterView

app_name = 'account'

urlpatterns = [
    path('signup', views.signup_view, name ="signup"),
    path('', views.login_view, name ="login"),
    path('login', views.login_view, name ="login"),
    path('logout', views.logout_view, name ="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
]