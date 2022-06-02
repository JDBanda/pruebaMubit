from django.test import SimpleTestCase #Librería basica de testing
from django.urls import reverse, resolve
from venta.views import Caja, Index

#Probar que las rutas si pasen por determinada vista
class TestUrls(SimpleTestCase):
    
    def test_index_url_resolve(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, Index)

    def test_caja_url_resolve(self):
        url = reverse('caja')
        self.assertEquals(resolve(url).func.view_class, Caja)