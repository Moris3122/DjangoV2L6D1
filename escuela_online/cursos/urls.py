from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_list, name='cursos_list'),
    path('crear/', views.crear_curso, name='crear_curso'),
    path('<int:id>/', views.detalle_curso, name='detalle_curso'),
    path('<int:id>/editar/', views.editar_curso, name='editar_curso'),
    path('<int:id>/eliminar/', views.eliminar_curso, name='eliminar_curso'),
]