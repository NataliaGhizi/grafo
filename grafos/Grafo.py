from Vertice import Vertice
from Aresta import Aresta

class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def retorna_vertices(self):
        return [v.getId() for v in self.lista_Vertices]

    def retorna_arestas(self):
        return ['id: {} - {}'.format(str(i), str(v)) for i, v in enumerate(self.lista_Arestas)]

    def remove_Aresta(self, a):
        del self.lista_Arestas[a]

    def desenha(self):
        retorno = []
        bar = 0
        tamanho = len(self.lista_Vertices)

        header = '\ |'
        for i in range(tamanho):
            header = header + ' {} |'.format(i)

        retorno.append(header)
        for vertice in self.lista_Vertices:
            batidas = [a.id for a in self.busca_Vizinhos(self.busca_Vertice(vertice.getId()))]

            linha = str(vertice) + ' |'
            for total in range(tamanho):
                if total == bar:
                    linha = linha + ' \ |'
                elif total in batidas:
                    linha = linha + ' x |'
                else:
                    linha = linha + '   |'
            bar += 1
            retorno.append(linha)
        return '\n'.join(retorno)
        
    def novo_Vertice(self, identificador):
        self.lista_Vertices.append(Vertice(identificador))

    def busca_Vertice(self, identificador):
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        
    def nova_Aresta(self, origem, destino, peso):
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))

    def busca_Vizinhos(self, u):
        retorno = []
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()

            if (u.getId() == origem.getId()):
                retorno.append(destino)
            elif (u.getId() == destino.getId()):
                retorno.append(origem)
        
        return retorno
    
    def busca_Adjacente(self, u):
        retorno = []
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) :
                destino.setVisitado(True)
                retorno.append(destino)
        
        return retorno
