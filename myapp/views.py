from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project,Tareas
from .forms import createNewTaks,createNewProject
# Create your views here.
def index(request):
    title = 'Django ok!!'
    return render(request, 'index.html', {
        'titulo': title
    })
def about(request):
    return render(request, 'about.html')

def projects(request):
    #projects = list(Project.objects.values()) 
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def taks(request):
    #tareas = Tareas.objects.get(id=id)
    #tareas = get_object_or_404(Tareas, id=id)
    tareas = Tareas.objects.all()
    return render(request, 'tasks/taks.html',{
        'tareas':tareas
    })

def create_taks(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_taks.html',{
            'form': createNewTaks()
        })
    else:
        Tareas.objects.create(titulo = request.POST['titulo'], descripcion = request.POST['descripcion'], project_id=1)
        return redirect('/taks/')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
        'form': createNewProject()
        })
    else:
        project = Project.objects.create(name = request.POST['name'])
        print(project)
        return render(request, 'projects/create_projects.html', {
        'form': createNewProject()
        })
    
    


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