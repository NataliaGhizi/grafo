class Aresta():
	def __init__(self,origem,destino):
		self.origem = origem
		self.destino = destino
				
	def getOrigem(self):
		return self.origem
		
	def getDestino(self):
		return self.destino
			
	def setOrigem(self,vertice):
		self.origem = vertice
		
	def setDestino(self,vertice):
		self.destino = vertice
	
	def __str__(self):
		return '{}-->{}'.format(self.origem.getId(), self.destino.getId())