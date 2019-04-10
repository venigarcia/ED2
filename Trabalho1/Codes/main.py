from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import argparse

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''
algoritmo = None
path_arquivo = None
param_a = None
param_b = None

parser = argparse.ArgumentParser(description='Ordenar os nodes do grafo gerado.')
parser.add_argument('--arquivo', required=True, dest='arq', help='Arquivo que desejas ordenar')
parser.add_argument('--sort', required=True, dest='sort', 
                    help='Algoritmo de ordenacao desejado: selectionsort, insertionsort, shellsort, mergesort, quicksort, heapsort, countsort')
'''
parser.add_argument('--insertionsort', help='Algoritmo de ordenacao desejado')
parser.add_argument('--selectionsort', help='Algoritmo de ordenacao desejado')
parser.add_argument('--shellsort', help='Algoritmo de ordenacao desejado')
parser.add_argument('--mergesort', help='Algoritmo de ordenacao desejado')
parser.add_argument('--quicksort', help='Algoritmo de ordenacao desejado')
parser.add_argument('--heapsort', help='Algoritmo de ordenacao desejado')
parser.add_argument('--countsort', help='Algoritmo de ordenacao desejado')
'''
parser.add_argument('--param_a', type=int, required=False,
                    help='valor de inicio para o QuickSort')
parser.add_argument('--param_b', type=int, required=False,
                    help='valor final para o QuickSort')

results = parser.parse_args()

if __name__ == "__main__":

    algoritimoDeOrdenacao = QuickSort()
    arquivoJson = '../Vertices/100vertices.json'
    arquivoDeSaida = '../Results/mst100Vertices.txt'

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)
