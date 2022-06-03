from django.db import models
from django.db.models import Sum, Avg
class turno(models.Model):
    persona_turno = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now=False, auto_now_add=True)
    cerrado = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self) -> str:
        return f'#{self.id} {self.persona_turno}'

    @property
    def total_sales(self):
        return sale.objects.filter(turno=turno.objects.get(id=self.id)).aggregate(Sum('amount'))
        
class SaleManager(models.Manager):
    def avg_client_pay(self):
        return sale.objects.all().aggregate(Avg('client_change'))

class sale(models.Model):
    amount = models.FloatField("Monto total de venta")
    client_change = models.FloatField("Cambio otorgado")
    date = models.DateTimeField("Fecha")
    turno = models.ForeignKey(turno,on_delete=models.CASCADE,null=True,blank=True)
    objects = SaleManager()
    
    def __str__(self):
        return "Id: "+str(self.id)+", cuenta: "+str(self.client_change)