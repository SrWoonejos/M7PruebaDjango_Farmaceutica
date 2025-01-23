from .laboratorio.models import Laboratorio, DirectorGeneral, Producto
from datetime import date

Laboratorio.objects.create(nombre="Laboratorio1")
Laboratorio.objects.create(nombre="Laboratorio2")
Laboratorio.objects.create(nombre="Laboratorio3")
Laboratorio.objects.create(nombre="Laboratorio4")
Laboratorio.objects.create(nombre="Laboratorio5")

dg1 = DirectorGeneral.objects.create(nombre="Director 1", laboratorio=Laboratorio.objects.get(nombre="Laboratorio1"))
dg2 = DirectorGeneral.objects.create(nombre="Director 2", laboratorio=Laboratorio.objects.get(nombre="Laboratorio2"))
dg3 = DirectorGeneral.objects.create(nombre="Director 3", laboratorio=Laboratorio.objects.get(nombre="Laboratorio3"))
dg4 = DirectorGeneral.objects.create(nombre="Director 4", laboratorio=Laboratorio.objects.get(nombre="Laboratorio4"))
dg5 = DirectorGeneral.objects.create(nombre="Director 5", laboratorio=Laboratorio.objects.get(nombre="Laboratorio5"))

Producto.objects.create(
    nombre="Producto 1",
    laboratorio=Laboratorio.objects.get(nombre="Laboratorio1"),
    f_fabricacion=date(2022, 5, 10),
    p_costo=1500.00,
    p_venta=2000.00
)

Producto.objects.create(
    nombre="Producto 2",
    laboratorio=Laboratorio.objects.get(nombre="Laboratorio2"),
    f_fabricacion=date(2021, 6, 15),
    p_costo=2500.00,
    p_venta=3000.00
)

Producto.objects.create(
    nombre="Producto 3",
    laboratorio=Laboratorio.objects.get(nombre="Laboratorio3"),
    f_fabricacion=date(2019, 8, 20),
    p_costo=3500.00,
    p_venta=4500.00
)

Producto.objects.create(
    nombre="Producto 4",
    laboratorio=Laboratorio.objects.get(nombre="Laboratorio4"),
    f_fabricacion=date(2023, 3, 25),
    p_costo=2000.00,
    p_venta=2600.00
)

Producto.objects.create(
    nombre="Producto 5",
    laboratorio=Laboratorio.objects.get(nombre="Laboratorio5"),
    f_fabricacion=date(2020, 12, 30),
    p_costo=3000.00,
    p_venta=4000.00
)
