import random
import sys
sys.setrecursionlimit(1000000)

'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''

# Sua classe algoritmo de ordenação precisar ter um método ordenar
class InsertionSort(object):
    def ordenar(self, colecao):
        for j in range(1, len(colecao)):
            chave = colecao[j]
            i = j-1
            while i>=0 and int(chave['weight']) < int(colecao[i]['weight']):
                colecao[i+1] = colecao[i]
                i-=1
            colecao[i+1] = chave

        return colecao

class SelectionSort(object):
    def ordenar(self, colecao):
        for i in range(0, len(colecao)-1):
            m = i
            for j in range(i, len(colecao)):
                if int(colecao[j]['weight']) < int(colecao[m]['weight']):
                    m = j
                colecao[m], colecao[i] = colecao[i], colecao[m]

        return colecao

class ShellSort(object):
    def ordenar(self, colecao):
        h = 1 #tem que ter para não bugar o incremento do piton
        for h in range(1, len(colecao), 3*h+1):
            while h > 0:
                h = int((h-1)/3)
                for i in range(h, len(colecao)):
                    temp = colecao[i]
                    j = i
                    while int(colecao[j-h]['weight']) > int(temp['weight']):
                        colecao[j] = colecao[j-h]
                        j = j - h
                        if j < h:
                            break
                    colecao[j] = temp
        return colecao

class MergeSort(object):
    def ordenar(self, colecao):
        if len(colecao) > 1:
            mid = int(len(colecao)/2)
            L = colecao[:mid]
            R = colecao[mid:]

            self.ordenar(L)
            self.ordenar(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if int(L[i]['weight']) < int(R[j]['weight']):
                    colecao[k] = L[i]
                    i+=1
                else:
                    colecao[k] = R[j]
                    j+=1
                k+=1
            
            while i < len(L):
                colecao[k] = L[i]
                i+=1
                k+=1
            while j < len(R):
                colecao[k] = R[j]
                j+=1
                k+=1
        
            return colecao

class QuickSort(object):
    def ordenar(self, colecao, inicio, fim, pivoType):
        if inicio < fim:
            posPivo = self.particiona(colecao, inicio, fim, pivoType)
            
            self.ordenar(colecao, inicio, posPivo-1, pivoType)
            self.ordenar(colecao, posPivo+1, fim, pivoType)
            
            return colecao

    def particiona(self, colecao, inicio, fim, pivoType):
        if pivoType == 2: #para o pivor ser um indice aleatório
            rndIndex = random.randint(inicio, fim)
            #joga o indice eleito para o fina do vetor
            colecao[rndIndex], colecao[fim] = colecao[fim], colecao[rndIndex]
        elif pivoType == 3: #para que o pivor seja a mediana do inicio e fim
            meio = int((inicio+fim)/2)
            a = int(colecao[inicio]['weight'])
            b = int(colecao[meio]['weight'])
            c = int(colecao[fim]['weight'])

            if a < b:
                if b < c:
                    mediana = meio
                else:
                    if a < c:
                        mediana = fim
                    else:
                        mediana = inicio
            else:
                if c < b:
                    mediana = meio
                else:
                    if c < a:
                        mediana = fim
                    else:
                        mediana = inicio            
            colecao[mediana], colecao[fim] = colecao[fim], colecao[mediana]

        pivo = int(colecao[fim]['weight'])
        i = (inicio - 1)

        for j in range(inicio, fim):
            if int(colecao[j]['weight']) <= pivo:
                i+=1
                colecao[i], colecao[j] = colecao[j], colecao[i]

        colecao[i+1], colecao[fim] = colecao[fim], colecao[i+1]
        return (i+1)

class HeapSort(object):
    def ordenar(self, colecao):
        n = len(colecao)

        for i in range(n, -1, -1):
            self.heapify(colecao, n, i)

        for i in range(n-1, 0, -1):
            colecao[i], colecao[0] = colecao[0], colecao[i]
            self.heapify(colecao, i, 0)
        
        return colecao
    
    def heapify(self, colecao, n, i):
        maior = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and int(colecao[i]['weight']) < int(colecao[l]['weight']):
            maior = l

        if r < n and int(colecao[maior]['weight']) < int(colecao[r]['weight']):
            maior = r
        
        if maior != i:
            colecao[i], colecao[maior] = colecao[maior], colecao[i]

            self.heapify(colecao, n, maior)

class CountSort(object):
    def ordenar(self, colecao):
        max_value = min_value = int(colecao[0]['weight'])
        for node in colecao:
            if int(node['weight']) > max_value:
                max_value = int(node['weight'])
            if int(node['weight']) < min_value:
                min_value = int(node['weight'])
        ran = max_value - min_value + 1
        count = [0]*ran
        output = [0]*len(colecao)
        for i in range(0, len(colecao)):
            count[int(colecao[i]['weight']) - min_value]+=1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        for i in range(len(colecao)-1, -1, -1):
            output[count[int(colecao[i]['weight']) - min_value] - 1] = colecao[i]
            count[int(colecao[i]['weight']) - min_value]-=1
        for i in range(0, len(colecao)):
            colecao[i] = output[i]
        
        return colecao
