from Grafo import Grafo
from utils.utils import *

def menu_geral():
    print('### MENU ###')
    print('1. Iniciar novo grafo')
    print('0. Sair')

    op = read_str("Opcao: ")
    if op == '1':
        menu_grafo()
    elif op == '0':
        return

def menu_grafo():
    print('\n### MENU GRAFO ###')

    tam_grafo = read_int("Defina a qtd. de vertices: ")

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
        print('0. Volvar')

        op = read_str("Opcao: ")
        if op == '1':
            op_a = 'h'
            while op_a == 'h':
                op_a = read_str("Informar o id dos vertices, origem e destino (ex.: 0 1), digite h para ajuda: ")

                if op_a == 'h':
                    print(g.retorna_vertices())

            origem, destino = op_a.split(' ')
            g.nova_Aresta(int(origem), int(destino), 1)

        elif op == '2':
            op_v = 'h'
            while op_v == 'h':
                op_v = read_str("Informar o id da aresta, digite h para ajuda: ")

                if op_v == 'h':
                    print(g.retorna_arestas())
            
            g.remove_Aresta(int(op_v))
        
        elif op == '3':
            op_l = 'h'
            while op_l == 'h':
                op_l = read_str("Informar o id do vertice, digite h para ajuda: ")

                if op_l == 'h':
                    print(g.retorna_vertices())
            
            dados = g.busca_Vizinhos(g.busca_Vertice(int(op_l)))
            print('Vizinhos de {}: '.format(op_l))
            for dado in dados:
                print(' \t - {}'.format(dado.id))
        
        elif op == '4':
            op_l = read_str("Informar o id do vertice, digite h para ajuda: ")
            dados = g.busca_Adjacente(g.busca_Vertice(int(op_l)))
            print('Adjacente de {}: '.format(op_l))
            for dado in dados:
                print(' \t - {}'.format(dado.id))
        
        elif op == '5':
            print(g.desenha())
            
        elif op == '0':
            return


while True:
    menu_geral()

print('boa noite')

