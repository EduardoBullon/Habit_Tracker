from django.urls import path
from . import views

urlpatterns = [
    path('mis-habitos/', views.listar_habitos, name='listar_habitos'),
    path('agregar-habito/', views.agregar_habito, name='agregar_habito'),
    path('progreso/', views.progreso, name='progress'),  # <-- Aquí
    path('registrar_habito/<int:hábito_id>/', views.registrar_habito, name='registrar_habito'),
    path('editar_habito/<int:hábito_id>/', views.editar_habito, name='editar_habito'),
    path('eliminar_habito/<int:hábito_id>/', views.eliminar_habito, name='eliminar_habito'),
]
