# para renderizar la template de django
from django.shortcuts import render
# modelos
from .models import *
# Fecha
import datetime
# Respuesta a solicitudes vía JSON
from django.http import JsonResponse
# Convertir a JSON
import json


def moneyChange(cantidad, cliente):
    """Calula el cambio devuelto.
    La función requiere de dos parámetros para obtener una resta de estos números,
    tal y como se lleva a cabo el proceso de dar cambio manualmente, es decir:
    Si el producto cuesta $35 pesos y recibo $50 el primer paso es restar el dinero que recibo
    menos lo que cuesta para obtener $25 de resultado.

    El siguiente paso es reducir el cambio a la mínia cantidad de billetes y pesos, para esto se
    usa la división exacta (// en python) para cada tipo de billete y moneda, el resultado se guarda
    en un diccionario que almacena el valor de cada elemento, es decir 2 billetes de X denominación.

    Existe el caso especial del 0.5 en el que se evalúa si el cambio es mayor o igual a 0.25 para
    devolver una moneda de 50 centavos, en caso contrario no devuelve cambio. Si el cambio es 0.99
    o menor a eso devolverá cincuenta centavos en cambio.

    Parámetros:
    cantidad -- valor numérico del monto total de vente
    cliente -- valor numérico del pago del cliente
    """
    moneyTuple = {
        "billete_500": 0,
        "billete_200": 0,
        "billete_100": 0,
        "billete_50": 0,
        "billete_20": 0,
        "moneda_10p": 0,
        "moneda_5p": 0,
        "moneda_2p": 0,
        "moneda_1p": 0,
        "moneda_50c": 0,
    }
    # Calcular cuanto se entrega de cambio
    cambio = float(cliente) - float(cantidad)
    # 1000
    if((cambio // 1000) > 0):
        moneyTuple["billete_1000"] = cambio // 1000
        cambio -= ((cambio // 1000) * 1000)
    # 500
    if((cambio // 500) > 0):
        moneyTuple["billete_500"] = cambio // 500
        cambio -= ((cambio // 500) * 500)
    # 200
    if((cambio // 200) > 0):
        moneyTuple["billete_200"] = cambio // 200
        cambio -= ((cambio // 200) * 200)
    # 100
    if((cambio // 100) > 0):
        moneyTuple["billete_100"] = cambio // 100
        cambio -= ((cambio // 100) * 100)
    # 50
    if((cambio // 50) > 0):
        moneyTuple["billete_50"] = cambio // 50
        cambio -= ((cambio // 50) * 50)
    # 20
    if((cambio // 20) > 0):
        moneyTuple["billete_20"] = cambio // 20
        cambio -= ((cambio // 20) * 20)
    # 10
    if((cambio // 10) > 0):
        moneyTuple["moneda_10p"] = cambio // 10
        cambio -= ((cambio // 10) * 10)
    # 5
    if((cambio // 5) > 0):
        moneyTuple["moneda_5p"] = cambio // 5
        cambio -= ((cambio // 5) * 5)
    # 2
    if((cambio // 2) > 0):
        moneyTuple["moneda_2p"] = cambio // 2
        cambio -= ((cambio // 2) * 2)
    # 1
    if((cambio // 1) > 0):
        moneyTuple["moneda_1p"] = cambio // 1
        cambio -= ((cambio // 1) * 1)
    # 0.5
    if((cambio // 0.5) > 0 or cambio >= 0.25):
        moneyTuple["moneda_50c"] = 1
        cambio = 0.5
    else:
        cambio = 0
    return moneyTuple


def index(request):
    # Cuando se procese un POST
    if (request.method == 'POST'):
        # Valores del front pasados por ajax
        amount = request.POST['amount']
        client_change = request.POST['client_change']
        try:
            # Registrar una venta
            newSale = sale(amount=amount,
                           client_change=client_change,
                           date=datetime.datetime.now())
            newSale.save()
            # Valor del cambio y función que devuelve un diccionario con los billetes
            cambio = float(client_change) - float(amount)
            # Devolución del cambio en formato JSON
            moneyDataJson = json.dumps(moneyChange(amount, client_change))
            # Respuesta satisfactoria
            return JsonResponse({
                'content': {
                    'title': 'Compra guardada',
                    'icon': 'success',
                    'data': moneyDataJson,
                    'cambio': cambio,
                }
            })
        except:
            # Respuesta no satisfactoria
            return JsonResponse({
                'content': {
                    'title': 'Error en la compra',
                    'icon': 'error',
                }
            })
    # Cuando no se procesa el POST devuelve la template unicamente
    context = {}
    return render(request, 'venta/index.html', context)
