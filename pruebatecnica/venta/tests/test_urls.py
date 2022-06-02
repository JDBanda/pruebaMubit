from django.test import SimpleTestCase
from django.urls import reverse, resolve
from venta.views import index

class TestUrls(SimpleTestCase):
    
    def test_index_url_resolve(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)