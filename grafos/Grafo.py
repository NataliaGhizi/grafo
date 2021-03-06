from Vertice import Vertice
from Aresta import Aresta

class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado

    def retorna_vertices(self):
        return [v.getId() for v in self.lista_Vertices]

    def retorna_arestas(self):
        return ['id: {} - {}'.format(str(i), str(v)) for i, v in enumerate(self.lista_Arestas)]

    def remove_aresta(self, a):
        del self.lista_Arestas[a]
    
    def retorna_qtd_aresta(self):
        return len(self.lista_Arestas)

    def existe_aresta(self, origem, destino):
        for a in self.lista_Arestas:
            if(str(a.getOrigem()) == origem and str(a.getDestino()) == destino):
                return True

        return False

    def atualizaQtdVizinho(self):
        for vertice in self.lista_Vertices:
            vizinhos = [a.id for a in self.busca_vizinhos(self.busca_vertice(vertice.getId()))]
            vertice.setVizinhos(len(vizinhos))

    def colorido(self):
        node_list = sorted(self.lista_Vertices, key=lambda x:x.getVizinhos(), reverse=True)
        col_val = {}

        for node in node_list:
            #print(node.id)

            available = [True] * len(node_list) 

            for adj_node in self.busca_vizinhos(self.busca_vertice(node.id)):
                if adj_node.id in col_val.keys():
                    col = col_val[adj_node.id]
                    available[col] = False
            clr = 0
            for clr in range(len(available)):
                if available[clr] == True:
                    break
            col_val[node.id] = clr

        return col_val
    
    def prim(self, nodo):
        # TODO
        # final = set()
        # inicio = True

        # while len(final) != len(self.lista_Vertices):
        #     if inicio:
        #         busca = nodo
        #         inicio = False

        #     franja = [str(v.id) for v in self.busca_vizinhos(self.busca_vertice(nodo))]
        #     lista_para_pegar_menor_peso = []
        #     for a in self.lista_Arestas:
        #         if str(a.getOrigem()) == str(busca) and str(a.getDestino()) in franja:
        #             lista_para_pegar_menor_peso.append(a)
        #     borda = sorted(lista_para_pegar_menor_peso, key=lambda e:e.getPeso())[0]
        #     busca = borda.getDestino()
            
        #     final.add(busca)

        

    def desenha(self):
        retorno = []
        bar = 0
        tamanho = len(self.lista_Vertices)

        header = '\ |'
        for i in range(tamanho):
            header = header + ' {} |'.format(i)

        retorno.append(header)
        for vertice in self.lista_Vertices:
            batidas = [a.id for a in self.busca_adjacente(self.busca_vertice(vertice.getId()))]

            linha = str(vertice) + ' |'
            for total in range(tamanho):
                if total == bar:
                    linha = linha + ' \ |'
                elif total in batidas:
                    linha = linha + ' 1 |'
                else:
                    linha = linha + ' 0 |'
            bar += 1
            retorno.append(linha)
        return '\n'.join(retorno)
        
    def novo_Vertice(self, identificador):
        self.lista_Vertices.append(Vertice(identificador))

    def busca_vertice(self, identificador):
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        
    def nova_aresta(self, origem, destino, peso):
        origem_aux = self.busca_vertice(origem)
        destino_aux = self.busca_vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux))

    def busca_vizinhos(self, u):
        retorno = []
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()

            if (u.getId() == origem.getId()):
                retorno.append(destino)
            elif (u.getId() == destino.getId()):
                retorno.append(origem)
        
        return retorno
    
    def busca_adjacente(self, u):
        retorno = []
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) :
                destino.setVisitado(True)
                retorno.append(destino)
        
        return retorno
