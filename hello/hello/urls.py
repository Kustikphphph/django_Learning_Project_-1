"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


#AAAAAAAAAAAAA

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('myform/', views.myform, name="myform"),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('form_up_img/', views.form_up_img, name='form_up_img'),
    path('form_up_img/delete_img/<int:id>/', views.delete_img),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)