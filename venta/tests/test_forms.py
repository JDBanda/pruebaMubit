from django.test import SimpleTestCase
from venta.forms import SaleForm

class TestForms(SimpleTestCase):
    def test_sale_form_is_valid(self):
        form = SaleForm({
            'amount':100,
            'client_change':500
        })
        self.assertTrue(form.is_valid())

    def test_sale_form_no_data(self):
        form = SaleForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)