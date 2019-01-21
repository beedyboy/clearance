"""blog URL Configuration
  url(r'^articles/', include('articles.urls')),
    url('admin/', admin.site.urls),
    url(r'^about/$',views.about),
    url('',views.homepage)
    
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from account.views import user_login, user_logout, success

urlpatterns = [

    path('', user_login),

    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),

    path('account/', include('account.urls')),
    path('system/', include('system.urls')),
    path('bursary/', include('bursary.urls')),
    path('admin/', admin.site.urls),

   # path('',article_views.article_list, name="home")

]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#urlpatterns.add(staticfiles_urlpatterns())