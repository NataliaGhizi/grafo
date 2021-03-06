from Grafo import Grafo
from utils.utils import *
import json

def menu_geral():
    while True:
        print('### MENU ###')
        print('1. Iniciar novo grafo')
        print('0. Sair')

        op = read_str("Opcao: ")
        if op == '1':
            menu_grafo()
        elif op == '0':
            break

def menu_grafo():
    print('\n### MENU GRAFO ###')

    #tam_grafo = read_int("Defina a qtd. de vertices: ")
    tam_grafo = 7

    g = Grafo()
    for i in range(tam_grafo):
        g.novo_Vertice(i)

    while True:
        print('\n')
        print('1. Nova aresta')
        print('2. Excluir aresta')
        print('3. Lista vizinhos')
        print('4. Lista adjacente')
        print('5. Desenha matriz')
        print('6. Cores - Welsh Powell')
        print('7. Prim')
        print('0. Voltar')

        op = read_str("Opcao: ")
        print(50 * '\n')
        if op == '1':
            # op_a = 'h'
            # while op_a == 'h':
            #     op_a = read_str("Informar o id dos vertices, origem, destino e peso (ex.: 0 1 5), digite h para ajuda: ")

            #     if op_a == 'h':
            #         print(g.retorna_vertices())

            # origem, destino, peso = op_a.split(' ')
            # if not g.existe_aresta(origem, destino):
            #    g.nova_aresta(int(origem), int(destino), int(peso))
            # else:
            #    print('aresta ja existe')
            g.nova_aresta(1,2,1)
            g.nova_aresta(1,3,3)
            g.nova_aresta(2,3,1)
            g.nova_aresta(2,4,2)
            g.nova_aresta(2,5,3)
            g.nova_aresta(3,5,2)
            g.nova_aresta(4,5,-3)

            g.nova_aresta(4,6,3)
            g.nova_aresta(5,6,2)
            

        elif op == '2':
            if g.retorna_qtd_aresta() > 0:
                op_v = 'h'
                while op_v == 'h':
                    op_v = read_str("Informar o id da aresta, digite h para ajuda: ")

                    if op_v == 'h':
                        print(g.retorna_arestas())
                
                g.remove_aresta(int(op_v))
            else:
                print('nenhuma aresta cadastrada')
        
        elif op == '3':
            op_l = 'h'
            while op_l == 'h':
                op_l = read_str("Informar o id do vertice, digite h para ajuda: ")

                if op_l == 'h':
                    print(g.retorna_vertices())
            
            dados = g.busca_vizinhos(g.busca_vertice(int(op_l)))
            print('Vizinhos de {}: '.format(op_l))
            for dado in dados:
                print(' \t - {}'.format(dado.id))
        
        elif op == '4':
            op_l = read_str("Informar o id do vertice, digite h para ajuda: ")
            dados = g.busca_adjacente(g.busca_vertice(int(op_l)))
            print('Adjacente de {}: '.format(op_l))
            for dado in dados:
                print(' \t - {}'.format(dado.id))
        
        elif op == '5':
            print(g.desenha())

        elif op == '6':
            g.atualizaQtdVizinho()
            print(json.dumps(g.colorido(), indent=4, sort_keys=True))
            print('* index do json = vertice e o valor do json = cor')

        elif op == '7':
            if g.retorna_qtd_aresta() > 0:
                op_v = 'h'
                while op_v == 'h':
                    op_v = read_str("Informar o id da aresta, digite h para ajuda: ")

                    if op_v == 'h':
                        print(g.retorna_arestas())
                
                g.prim(int(op_v))
            else:
                print('nenhuma aresta cadastrada')
            
        elif op == '0':
            return

menu_geral()

print('boa noite')

