from modificar_formulas.models import Inventario

class Formulas:

	def sumatoria(indices, opcion):
		return "Filas seleccionadas para SUMATORIA: "+str(len(indices))

	def promedio(indices, opcion):
		return "Filas seleccionadas para PROMEDIO: "+str(len(indices))