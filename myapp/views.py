from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,Tareas
# Create your views here.
def index(request):
    return HttpResponse("<h1> Index page</h1>")
def hello(request, usuario):
    print(usuario)
    return HttpResponse("<h1>Hello %s</h1> "% usuario) # uso de parametros: puede ser str, int, etc
def about(request):
    return HttpResponse("<h3>mas de nosotros.!</h3>")

# seccion para hacer  consultas.
def projects(request):
    projects = list(Project.objects.values()) 
    return JsonResponse(projects, safe = False)
def taks(request, id):
    tareas = Tareas.objects.get(id=id)
    return HttpResponse('tarea: %s'% tareas.titulo)