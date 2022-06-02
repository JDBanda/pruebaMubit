from django.test import TestCase, Client
from django.urls import reverse
from venta.models import *
import json

#Comprobar por medio de un cliente http la respuesta 200 y que se use la plantilla
class TestViews(TestCase):
    #Se puede optar por colocar una definición en el método setUp
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.caja_url = reverse('caja')

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'venta/turno.html')

    def test_caja_GET(self):
        response = self.client.get(self.caja_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'venta/caja.html')

    def test_turno_creation(self):
        response = self.client.post(self.index_url, {
            'usuario': 'Joaquin23'
        })
        self.assertEquals(response.status_code, 302)

    def test_sale_creation(self):
        turno_test = turno.objects.create(persona_turno="Pedro")
        response = self.client.post(self.caja_url, {
            'amount':500,
            'client_change':200,
            'cashier':turno_test.id
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(sale.objects.last().turno, turno_test)

    # Situación en donde un test corrige código
    def test_sale_creation_no_parameters(self):
        response = self.client.post(self.caja_url)
        self.assertEquals(response.status_code, 404)

    def test_sale_creation_strings_params(self):
        turno_test = turno.objects.create(persona_turno="Pedro")
        response = self.client.post(self.caja_url, {
            'amount':'$200',
            'client_change':'$500',
            'cashier':turno_test.id
        })
        self.assertEquals(response.status_code, 400)