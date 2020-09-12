"""alcon2019j URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import manager.views as manager_view

urlpatterns = [
    #ホームページのディレクトリ構成みたいな?
    path('admin/', admin.site.urls),
    path('Home/', manager_view.HomeView.as_view(),name='home'),
    path('worker_list/', manager_view.WorkerListView.as_view(),name='worker_list'),
    path('skill_reg/', manager_view.SkillRegisterView.as_view(),name='skill_reg'),
    path('worker_reg/', manager_view.WorkerRegisterView.as_view(),name='worker_reg'),
    path('worker_skill_reg/',manager_view.WorkerSkillRegisterView.as_view(),name='worker_skill_reg')
]
