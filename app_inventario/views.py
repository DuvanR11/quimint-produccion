from django.conf import Settings
from django.shortcuts import render
import numpy as np 
from matplotlib import pyplot
import sys
import os
from .models import *
import matplotlib.pyplot as plt

# Create your views here.

# Entradas
def agregarEquipos(request):
    return render(request, 'pages/equipos/entradas_equipos.html')

def agregarHerramientas(request):
    return render(request, 'pages/herramientas/entradas_herramientas.html')

def agregarSumistros(request):
    return render(request, 'pages/suministros/entradas_suministros.html')

# salidas



# Dashboard
def dashboardEquipos(request):
    # try:
    #     pedidos = Equipos.objects.values('nombre')\
    #         .annotate(cantidad = sum('cantidad'))\
    #         .values('nombre', 'cantidad')
    #         # 
    #     cantidades = []
    #     nombreProductos = []
    #     for p in pedidos:
    #         pro = Equipos.objects.get(id=p['nombre'])
    #         nombreProductos.append(pro.nombre)
    #         cantidades.append(int(p['cantidad']))
    #         # 
    #     pyplot.title('Cantidad de salida de equipos')
    #     pyplot.xlabel('Productos')
    #     pyplot.ylabel('Cantidad')
    #     pyplot.barh(nombreProductos, cantidades)
    #     rutaImagen = os.pathjoin(Settings.MEDIA_ROOT + "\\" + "grafica.png")
    #     pyplot.savefig(rutaImagen)
    # except:
    #    print('error')
    
    fig, ax = plt.subplots()

    meses = ['Julio', 'Agosto', 'Septiembre', 'Octubre']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(meses, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Meses')
    ax.set_title('Registro de Equipos')
    ax.legend(title='Meses')

    plt.show()
    return render(request, 'pages/equipos/entradas_equipos.html')