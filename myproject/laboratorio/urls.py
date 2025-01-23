from django.urls import path
from . import views

urlpatterns = [
    # URLs para Laboratorio
    path('', views.laboratorio_list, name='laboratorio-list'),
    path('laboratorios/<int:pk>/', views.laboratorio_detail, name='laboratorio-detail'),
    path('laboratorios/create/', views.laboratorio_create, name='laboratorio-create'),
    path('laboratorios/<int:pk>/update/', views.laboratorio_update, name='laboratorio-update'),
    path('laboratorios/<int:pk>/delete/', views.laboratorio_delete, name='laboratorio-delete'),

    # URLs para DirectorGeneral
    path('directores/', views.director_list, name='director-list'),
    path('directores/<int:pk>/', views.director_detail, name='director-detail'),
    path('directores/create/', views.director_create, name='director-create'),
    path('directores/<int:pk>/update/', views.director_update, name='director-update'),
    path('directores/<int:pk>/delete/', views.director_delete, name='director-delete'),

    # URLs para Producto
    path('productos/', views.producto_list, name='producto-list'),
    path('productos/<int:pk>/', views.producto_detail, name='producto-detail'),
    path('productos/create/', views.producto_create, name='producto-create'),
    path('productos/<int:pk>/update/', views.producto_update, name='producto-update'),
    path('productos/<int:pk>/delete/', views.producto_delete, name='producto-delete'),
]
