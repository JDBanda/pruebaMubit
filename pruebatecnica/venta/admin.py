from django.contrib import admin
from .models import *

# Register your models here.

# Valores a mostrar en el administrador


class saleAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount',
                    'client_change', 'date']
    ordering = ['date']


# Register your models here.
admin.site.register(sale, saleAdmin)
