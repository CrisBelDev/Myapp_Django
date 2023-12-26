from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:usuario>', views.hello),
    path('projects/', views.projects),
    path('taks/', views.taks),
    path('create_taks/', views.create_taks),
    path('create_project/',views.create_project),
]