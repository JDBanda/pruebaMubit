from django.db import models

# Create your models here.
class sale(models.Model):
    amount = models.FloatField("Monto total de venta")
    client_change = models.FloatField("Cambio otorgado")
    date = models.DateTimeField("Fecha")

    def __str__(self):
        return "Id: "+str(self.id)+", cuenta: "+str(self.client_change)