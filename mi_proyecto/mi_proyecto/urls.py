from django.contrib import admin
from django.urls import path
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('verificar-token/', views.verificar_usuario, name='verificar_token'),
    path('', views.index, name='login'),  # ruta raíz al index
]
