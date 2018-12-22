from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('department/new', views.create_dept, name ="dept_create"),
    path('', views.create_faculty, name="fac_create"),
    path('faculty/add', views.add_faculty, name="addFaculty"),
]