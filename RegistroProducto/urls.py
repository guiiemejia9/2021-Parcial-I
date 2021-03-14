"""RegistroProducto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Categoria.views import FormularioCategoriaView
from Models.Marca.views import FormularioMarcaView
from Models.Producto.views import FormularioProductoView
from Views.Controladores import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('registrarMarca/',FormularioMarcaView.index, name='registrarMarca'),
    path('guardarMarca/',FormularioMarcaView.procesar_formulario, name='guardarMarca'),
    path('listaMarcas/',FormularioMarcaView.listar_marca, name='listaMarcas'),
    path('editarMarcas/<int:id_marca>', FormularioMarcaView.edit, name='editarMarcas'),
    path('actualizarMarcas/<int:id_marca>', FormularioMarcaView.actualizar_marca, name='actualizarMarcas'),
    path('eliminarMarcas/<int:id_marca>', FormularioMarcaView.delete, name='eliminarMarcas'),
    path('registrarCategoria/',FormularioCategoriaView.index, name='registrarCategoria'),
    path('guardarCategoria/',FormularioCategoriaView.procesar_formulario, name='guardarCategoria'),
    path('listaCategorias/',FormularioCategoriaView.listar_categoria, name='listaCategorias'),
    path('editarCategorias/<int:id_categoria>', FormularioCategoriaView.edit, name='editarCategorias'),
    path('actualizarCategorias/<int:id_categoria>', FormularioCategoriaView.actualizar_categoria, name='actualizarCategorias'),
    path('eliminarCategorias/<int:id_categoria>', FormularioCategoriaView.delete, name='eliminarCategorias'),
    path('registrarProducto/',FormularioProductoView.index, name='registrarProducto'),
    path('guardarProducto/',FormularioProductoView.procesar_formulario, name='guardarProducto'),
    path('listaProductos/',FormularioProductoView.listar_producto, name='listaProductos'),
    path('editarProductos/<int:id_producto>', FormularioProductoView.edit, name='editarProductos'),
    path('actualizarProductos/<int:id_producto>', FormularioProductoView.actualizar_producto, name='actualizarProductos'),
    path('eliminarProductos/<int:id_producto>', FormularioProductoView.delete, name='eliminarProductos'),
]
