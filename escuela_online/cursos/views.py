from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos_list.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos_list')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})

def detalle_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos_list')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})