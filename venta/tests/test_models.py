from django.test import TestCase
from venta.models import sale, turno

class TestModels(TestCase):
    def setUp(self):
        self.turno1 = turno.objects.create(persona_turno="Jhonny")
        self.turno2 = turno.objects.create(persona_turno="Violet")
        self.sale1 = sale.objects.create(
            amount=60,client_change=550,turno=self.turno1,date="2022-06-1"
        )
        self.sale2 = sale.objects.create(
            amount=101,client_change=301,turno=self.turno1,date="2022-06-1"
        )
        self.sale3 = sale.objects.create(
            amount=140,client_change=140,turno=self.turno2,date="2022-06-2"
        )
        self.sale4 = sale.objects.create(
            amount=11,client_change=51,turno=self.turno2,date="2022-06-2"
        )
        self.sale5 = sale.objects.create(
            amount=4,client_change=20,turno=self.turno2,date="2022-06-2"
        )
        self.avg = sale.objects.avg_client_pay()["client_change__avg"]

    def test_total_amount_by_turno(self):
        self.assertGreaterEqual(self.turno1.total_sales["amount__sum"],100)

    def test_avg_client_pay(self):
        self.assertGreaterEqual(self.avg,200)