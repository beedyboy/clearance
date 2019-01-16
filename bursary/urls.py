from django.urls import path

from . import views

app_name = 'bursary'

urlpatterns = [

     path('', views.create_fee, name ="home"), #for url like bursary/bursary/new
     path('fees/new', views.create_fee, name ="create_fee"), #for url like bursary/bursary/new
     path('fees/save', views.save_fee, name ="addFee"), #for url like bursary/bursary/save
     path('fees/<int:pk>/edit', views.edit_fee, name="edit_fee"), #for url like bursary/session/1/edit
      #path('', views.SignUpView.as_view(), name ="SignUpView"),
     path('fees/get_department/', views.get_department, name ="get_department"),
]
