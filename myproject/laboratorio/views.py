from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio, DirectorGeneral, Producto


# --- CRUD para Laboratorio ---
def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/list.html', {'laboratorios': laboratorios})


def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'laboratorio/detail.html', {'laboratorio': laboratorio})


def laboratorio_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad', 'Santiago')
        pais = request.POST.get('pais', 'Chile')
        Laboratorio.objects.create(nombre=nombre, ciudad=ciudad, pais=pais)
        return redirect('laboratorio-list')
    return render(request, 'laboratorio/form.html')


def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.nombre = request.POST.get('nombre')
        laboratorio.ciudad = request.POST.get('ciudad', 'Santiago')
        laboratorio.pais = request.POST.get('pais', 'Chile')
        laboratorio.save()
        return redirect('laboratorio-list')
    return render(request, 'laboratorio/form.html', {'laboratorio': laboratorio})


def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio-list')
    return render(request, 'laboratorio/confirm_delete.html', {'laboratorio': laboratorio})


# --- CRUD para DirectorGeneral ---
def director_list(request):
    directores = DirectorGeneral.objects.all()
    return render(request, 'director/list.html', {'directores': directores})


def director_detail(request, pk):
    director = get_object_or_404(DirectorGeneral, pk=pk)
    return render(request, 'director/detail.html', {'director': director})


def director_create(request):
    laboratorios = Laboratorio.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        laboratorio_id = request.POST.get('laboratorio')
        especialidad = request.POST.get('especialidad', 'Medicina General')
        laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
        DirectorGeneral.objects.create(nombre=nombre, laboratorio=laboratorio, especialidad=especialidad)
        return redirect('director-list')
    return render(request, 'director/form.html', {'laboratorios': laboratorios})


def director_update(request, pk):
    director = get_object_or_404(DirectorGeneral, pk=pk)
    laboratorios = Laboratorio.objects.all()
    if request.method == 'POST':
        director.nombre = request.POST.get('nombre')
        laboratorio_id = request.POST.get('laboratorio')
        director.laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
        director.especialidad = request.POST.get('especialidad', 'Medicina General')
        director.save()
        return redirect('director-list')
    return render(request, 'director/form.html', {'director': director, 'laboratorios': laboratorios})


def director_delete(request, pk):
    director = get_object_or_404(DirectorGeneral, pk=pk)
    if request.method == 'POST':
        director.delete()
        return redirect('director-list')
    return render(request, 'director/confirm_delete.html', {'director': director})


# --- CRUD para Producto ---
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto/list.html', {'productos': productos})


def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/detail.html', {'producto': producto})


def producto_create(request):
    laboratorios = Laboratorio.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        laboratorio_id = request.POST.get('laboratorio')
        f_fabricacion = request.POST.get('f_fabricacion')
        p_costo = request.POST.get('p_costo')
        p_venta = request.POST.get('p_venta')
        laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
        Producto.objects.create(
            nombre=nombre,
            laboratorio=laboratorio,
            f_fabricacion=f_fabricacion,
            p_costo=p_costo,
            p_venta=p_venta
        )
        return redirect('producto-list')
    return render(request, 'producto/form.html', {'laboratorios': laboratorios})


def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    laboratorios = Laboratorio.objects.all()
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        laboratorio_id = request.POST.get('laboratorio')
        producto.laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
        producto.f_fabricacion = request.POST.get('f_fabricacion')
        producto.p_costo = request.POST.get('p_costo')
        producto.p_venta = request.POST.get('p_venta')
        producto.save()
        return redirect('producto-list')
    return render(request, 'producto/form.html', {'producto': producto, 'laboratorios': laboratorios})


def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto-list')
    return render(request, 'producto/confirm_delete.html', {'producto': producto})
