from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Inventario(models.Model):
	codigo = models.CharField(max_length=4)
	descripcion = models.CharField(max_length=200)
	valor_unitario = models.DecimalField(max_digits=8, decimal_places=2)
	cantidades = models.IntegerField(default=0)

	def __str__(self):
		return self.descripcion