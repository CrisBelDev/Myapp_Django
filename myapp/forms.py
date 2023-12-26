from django import forms

class createNewTaks(forms.Form):
    titulo = forms.CharField(label='titulo de tarea', max_length=200)
    descripcion = forms.CharField(label='descripcion de tarea', widget=forms.Textarea)
class createNewProject(forms.Form):
    name = forms.CharField(label="nombre de proyecto: ", max_length=200)