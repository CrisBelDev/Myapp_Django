from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.index, name ='index'),
    path('about/', views.about, name ='about'),
    path('hello/<str:usuario>', views.hello, name ='hello'),
    path('projects/', views.projects, name ='projects'), 
    path('taks/', views.taks, name ='taks'),
    path('create_taks/', views.create_taks, name ='create_taks'),
    path('create_project/',views.create_project, name ='create_projects'),
]