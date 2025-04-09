from django.contrib import admin
from django.urls import path, include
from tracker import views  # Asegúrate de importar el archivo views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página principal
    path('accounts/', include('django.contrib.auth.urls')),
    path('mis-habitos/', include('tracker.urls')),  # Aquí no se debe duplicar la ruta ''
]
