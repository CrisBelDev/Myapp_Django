from django.db import models

# scrib para la base de datos (ejm. my sql, postgres, ...)
class Project(models.Model):
    name = models.CharField(max_length=200)

class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE)



