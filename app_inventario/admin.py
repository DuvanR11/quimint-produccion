from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class categoriasAdmin(admin.ModelAdmin):
    pass    

class EquiposAdmin(admin.ModelAdmin):
    list_filter = ['estado']
    list_display = [ 'nombre', 'referencia',  'ordenEmitida', 'enviadoalArea','solicitudDeMantenimiento', 'ocupadoenArea', 'observaciones', 'marca', 'valorU', 'costo', 'cantidad', 'entrada', 'sacar', 'disponible', 'estados', '_', 'foto']
    search_fields = ['fecha', 'nombre', 'referencia', 'estado', 'cantidad', 'ordenEmitida', 'enviadoalArea','solicitudDeMantenimiento', 'ocupadoenArea', 'observaciones', 'imagenE', 'marca', 'valorU', 'costo']
    actions = ['salida']
    list_per_page: 12
    

    def entrada(self, obj):
        return format_html('<a href="/">Entrada</a>')
    
    def sacar(self, obj):
        return format_html('<a href="/">salida</a>')
        
    def disponible(self, obj):
       disponibla = obj.cantidad - obj.salida
       return disponibla
   
    # Funcion para estados
    def _(self, obj):
        disponibla = obj.cantidad - obj.salida
        if disponibla >= 10:
            obj.estado == 'Disponible'
            return True
        elif disponibla <= 10:
            obj.estado == 'Pocas'
            return None
        else: 
            return False
    _.boolean = True
    
    def estados(self, obj):
        disponibla = obj.cantidad - obj.salida
        if disponibla >= 10:
            obj.estado = 'Disponible'
            color = '#28a745'
        elif disponibla <= 10:
            obj.estado = 'Pocas'
            color = '#fea95e'
        else: 
            color = 'red'
        return format_html('<strong><p style = "color:{}">{}</p></strong'.format(color, obj.estado))
    estados.allow_tags = True
    
    def foto(self, obj):
        return format_html('<img src={} width="100" height="80"/>',  obj.imagenE.url)
    
    

class SuministrosAdmin(admin.ModelAdmin):
    pass

class HerramientasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Equipos, EquiposAdmin)
admin.site.register(Suministros, SuministrosAdmin)
admin.site.register(Herramientas, HerramientasAdmin)