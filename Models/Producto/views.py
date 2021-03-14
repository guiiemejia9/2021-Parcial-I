from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from Models.Producto.forms import FormularioProducto
from Models.Producto.models import Producto


class FormularioProductoView(HttpRequest):
    def index(request):
        producto =FormularioProducto()
        return render(request,"ProductoIndex.html",{"form":producto})

    #recibe la peticion del navegador (request),valida la informacion y guarda
    def procesar_formulario(request):
        producto =FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto =FormularioProducto()
        return render(request,"ProductoIndex.html",{"form":producto,"mensaje": 'ok'})

    def listar_producto(request):
        productos = Producto.objects.all()
        return  render(request,"listaProductos.html", {"productos": productos})

    def edit(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form= FormularioProducto(instance=producto)
        return  render(request,"EditarProducto.html", {"form":form,"producto": producto})

    def actualizar_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
        return render(request, "listaProductos.html", {"productos": productos,"mensaje": 'ok'})

    def delete(request,id_producto):
        producto= Producto.objects.get(pk=id_producto)
        producto.delete()
        productos=Producto.objects.all()
        return render(request, "listaProductos.html", {"productos": productos,"mensaje2": 'ok'})