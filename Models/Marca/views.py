from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from Models.Marca.forms import FormularioMarca
from Models.Marca.models import Marca

class FormularioMarcaView(HttpRequest):
    def index(request):
        marca =FormularioMarca()
        return render(request,"MarcaIndex.html",{"form":marca})

    #recibe la peticion del navegador (request),valida la informacion y guarda
    def procesar_formulario(request):
        marca =FormularioMarca(request.POST)
        if marca.is_valid():
            marca.save()
            marca =FormularioMarca()
        return render(request,"MarcaIndex.html",{"form":marca,"mensaje": 'ok'})

    def listar_marca(request):
        marcas = Marca.objects.all()
        return  render(request,"listaMarcas.html", {"marcas": marcas})

    def edit(request, id_marca):
        marca = Marca.objects.filter(id=id_marca).first()
        form= FormularioMarca(instance=marca)
        return  render(request,"EditarMarca.html", {"form":form,"marca": marca})

    def actualizar_marca(request, id_marca):
        marca = Marca.objects.get(pk=id_marca)
        form = FormularioMarca(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            marcas = Marca.objects.all()
        return render(request, "listaMarcas.html", {"marcas": marcas,"mensaje": 'ok'})

    def delete(request,id_marca):
        marca= Marca.objects.get(pk=id_marca)
        marca.delete()
        marcas=Marca.objects.all()
        return render(request, "listaMarcas.html", {"marcas": marcas,"mensaje2": 'ok'})


