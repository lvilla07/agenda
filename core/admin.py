from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin): #permite ao evento abrir todos os campos informados abaixo
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',) #adiciona uma lista de filtros a visualizacao dos eventos



admin.site.register(Evento, EventoAdmin)
