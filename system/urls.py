from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('', views.create_faculty, name="fac_create"), #for url like system/
    path('faculty', views.view_faculty, name="fac_view"), #for url like system/faculty
    path('faculty/<int:pk>/edit', views.fac_link_edit, name="fac_link_edit"), #for url like system/faculty
    path('faculty/<int:id>/view', views.fac_link_view, name="fac_link_view"), #for url like system/faculty
    path('faculty/new', views.create_faculty, name="fac_create"),#for url like system/faculty/new
    path('faculty/save', views.add_faculty, name="addFaculty"),#for url like system/faculty/new


    path('department', views.create_dept, name ="dept"), #for url like system/department/new
    path('department/new', views.create_dept, name ="dept_create"), #for url like system/department/new
    path('department/save', views.add_dept, name ="addDept"), #for url like system/department/save

    path('session/new', views.create_session, name ="session_create"), #for url like system/session/new
    path('session/save', views.add_session, name ="addSession"), #for url like system/session/save
    path('session/<int:pk>/edit', views.session_edit, name="session_edit"), #for url like system/session/1/edit

     path('semester/new', views.create_semester, name ="create_semester"), #for url like system/semester/new
    path('semester/save', views.add_semester, name ="addSemester"), #for url like system/semester/save
]