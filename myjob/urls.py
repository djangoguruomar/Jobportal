"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path("", views.CategoryListView.as_view(), name="home"),
    path('signup/', views.register, name='signup'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('new_jobs/', views.JobCreate.as_view(), name='create-jobs'),
    path('job_delete/<int:pk>/', views.JobDelete.as_view(), name='delete-jobs'),
    path('job_update/<int:pk>/', views.JobUpdate.as_view(), name='update-jobs'),
    path('jobs/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),
    path('jobseeker/', views.JobSeekerListView.as_view(), name='jobseeker'),
    path('jobseeker/<int:pk>', views.JobSeekerDetailView.as_view(), name='jobseeker-detail'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),

    path('home', views.home)
    
    
    ]
