from django.shortcuts import render, redirect, get_object_or_404
from .models import Hábito, RegistroHábito
from django.contrib.auth.decorators import login_required

# Vista para agregar un hábito
@login_required
def agregar_habito(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        frecuencia = request.POST['frecuencia']

        # Crear un nuevo hábito en la base de datos
        Hábito.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            usuario=request.user,
            frecuencia=frecuencia
        )

        # Redirigir al usuario a la lista de hábitos
        return redirect('listar_habitos')

    return render(request, 'tracker/agregar_habito.html')


# Vista para listar los hábitos
@login_required
def listar_habitos(request):
    # Obtener todos los hábitos del usuario logueado
    hábitos = Hábito.objects.filter(usuario=request.user)
    return render(request, 'tracker/listar_habitos.html', {'hábitos': hábitos})


# Vista para registrar el progreso de un hábito
@login_required
def registrar_habito(request, hábito_id):
    hábito = get_object_or_404(Hábito, id=hábito_id)

    if request.method == 'POST':
        # Verificar si el hábito fue completado
        completado = 'completado' in request.POST

        # Registrar el progreso del hábito
        RegistroHábito.objects.create(hábito=hábito, completado=completado)

        # Redirigir al usuario a la lista de hábitos
        return redirect('listar_habitos')

    return render(request, 'tracker/registrar_habito.html', {'hábito': hábito})


# Vista para editar un hábito
@login_required
def editar_habito(request, hábito_id):
    hábito = get_object_or_404(Hábito, id=hábito_id)

    if request.method == 'POST':
        # Actualizar los datos del hábito
        hábito.nombre = request.POST['nombre']
        hábito.descripcion = request.POST['descripcion']
        hábito.frecuencia = request.POST['frecuencia']
        hábito.save()

        # Redirigir a la lista de hábitos
        return redirect('listar_habitos')

    return render(request, 'tracker/editar_habito.html', {'hábito': hábito})


# Vista para eliminar un hábito
@login_required
def eliminar_habito(request, hábito_id):
    hábito = get_object_or_404(Hábito, id=hábito_id)

    # Eliminar el hábito
    hábito.delete()

    # Redirigir a la lista de hábitos
    return redirect('listar_habitos')
