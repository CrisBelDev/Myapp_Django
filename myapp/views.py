from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Project,Tareas
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values()) 
    return render(request, 'projects.html')
def taks(request):
    #tareas = Tareas.objects.get(id=id)
    #tareas = get_object_or_404(Tareas, id=id)
    return render(request, 'taks.html')



def hello(request, usuario):
    print(usuario)
    return HttpResponse("<h1>Hello %s</h1> "% usuario) # uso de parametros: puede ser str, int, etc

'''
# seccion para hacer  consultas.
def projects(request):
    projects = list(Project.objects.values()) 
    return JsonResponse(projects, safe = False)
def taks(request, id):
    #tareas = Tareas.objects.get(id=id)
    tareas = get_object_or_404(Tareas, id=id)
    return HttpResponse('tarea: %s'% tareas.titulo)
'''