class Vertice():
    def __init__(self, id):
        self.id = id
        self.visitado = False

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id
    
    def setVizinhos(self, vizinhos):
        self.vizinhos = vizinhos
    
    def getVizinhos(self):
        return self.vizinhos

    def __str__(self):
        return str(self.id)
