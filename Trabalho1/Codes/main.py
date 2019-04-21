from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import argparse
import cProfile, pstats, io
import json

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

parser = argparse.ArgumentParser(description='Ordenar os nodes do grafo gerado.')
parser.add_argument('--arquivo', type=str, required=True, dest='arq', help='Caminho para o arquivo que desejas ordenar')
parser.add_argument('--saida', type=str, dest='save', help='Caminho para salvar o arquivo ordenado e o Log da execução')
parser.add_argument('--insertionsort', dest='insert', action='store_true', help='Algoritmo de ordenacaoo InsertionSort')
parser.add_argument('--selectionsort', dest='select', action='store_true', help='Algoritmo de ordenacao SelectionSort')
parser.add_argument('--shellsort', dest='shell', action='store_true', help='Algoritmo de ordenacao ShellSort')
parser.add_argument('--mergesort', dest='merge', action='store_true', help='Algoritmo de ordenacao MergeSort')
parser.add_argument('--quicksort', dest='quick', action='store_true', help='Algoritmo de ordenacao QuickSort --param_a = tipo de pivô')
parser.add_argument('--heapsort', dest='heap', action='store_true', help='Algoritmo de ordenacao HeapSort')
parser.add_argument('--countsort', dest='count', action='store_true', help='Algoritmo de ordenacao CountSort')
parser.add_argument('--pivo', dest='pivo', type=int, default=None, required=False, help='Tipo de pivo para o QuickSort 1 - Inicio e Fim 2 - Aleatório 3 - Mediana')

args = parser.parse_args()

if __name__ == "__main__":
    if args.insert:
        algoritimoDeOrdenacao = InsertionSort()
    elif args.select:
        algoritimoDeOrdenacao = SelectionSort()
    elif args.shell:
        algoritimoDeOrdenacao = ShellSort()
    elif args.merge:
        algoritimoDeOrdenacao = MergeSort()
    elif args.quick:
        algoritimoDeOrdenacao = QuickSort()
    elif args.heap:
        algoritimoDeOrdenacao = HeapSort()
    elif args.count:
        algoritimoDeOrdenacao = CountSort()

    arquivoJson = args.arq
    arquivoDeSaida = args.save
    print()
    print(arquivoDeSaida)
    print()
    for i in range(len(arquivoDeSaida)-6, -1, -1):
        if arquivoDeSaida[i] == '\\':
            break
    logFile = arquivoDeSaida[-(len(arquivoDeSaida)-1-i):-4]
    algo = []
    algos = [InsertionSort(), SelectionSort(), ShellSort(), MergeSort(), QuickSort(), HeapSort(), CountSort()]
    final_val = []
    for algo in algos:     
        pr = cProfile.Profile()
        pr.enable()
        
        grafo = Grafo()
        grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao, args.pivo)
        grafo.carregarGrafo(arquivoJson)
        arvoreGeradoraMinima =  grafo.executarKruskal()
        SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)
        
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
        ps.print_stats()

        out = s.getvalue()
        count = 0
        start = 0
        end = 0
        for i in range(9, len(out)):
            if out[i] == ' ':
                count+=1
            if count == 4 and start == 0:
                start = i+1
            if count == 5 and end == 0:
                end = i
                break
        val=float(out[start:end])
        final_val.append(val)

    final_dict = {"InsertionSort":final_val[0], "SelectionSort":final_val[1], "ShellSort":final_val[2], "MergeSort":final_val[3], "QuickSort":final_val[4], "HeapSort":final_val[5], "CountSort":final_val[6]}
    with open("../LogFiles/" + logFile + ".json", 'w+') as f:
        json.dump(final_dict, f)