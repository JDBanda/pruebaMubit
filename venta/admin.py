from django.contrib import admin
from .models import *
@admin.register(sale)
class saleAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount',
                    'client_change', 'date']
    ordering = ['date']

@admin.register(turno)
class turnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona_turno', 'creado', 'cerrado')