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
        '''
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
        '''
        for j in range(1, len(colecao)):
            chave = int(colecao[j]['weight'])
            i = j-1
            while i>=0 and int(colecao[i]['weight']) > chave:
                colecao[i+1]['weight'] = int(colecao[i]['weight'])
                i-=1
        colecao[i+1]['weight'] = chave
        
        return colecao

class SelectionSort(object):
    def ordenar(self, colecao):
        for i in range(0, len(colecao)-1):
            m = i
            for j in range(i, len(colecao)):
                if int(colecao[j]['weight']) < int(colecao[m]['weight']):
                    m = j
                temp = colecao[m]
                colecao[m] = colecao[i]
                colecao[i] = temp

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
    def ordenar(self, colecao, inicio, fim):
        #print("Ordena: " + str(inicio) + " " + str(fim))
        if inicio < fim:
            posPivo = self.particiona(colecao, inicio, fim)
            
            self.ordenar(colecao, inicio, posPivo-1)
            self.ordenar(colecao, posPivo+1, fim)
            
            return colecao

    def particiona(self, colecao, inicio, fim):
        #print("Particiona: " + str(inicio) + " " + str(fim))
        pivo = int(colecao[fim]['weight'])
        i = (inicio - 1)

        for j in range(inicio, fim):
            if int(colecao[j]['weight']) <= pivo:
                i+=1
                colecao[i], colecao[j] = colecao[j], colecao[i]

        colecao[i+1], colecao[fim] = colecao[fim], colecao[i+1]
        return (i+1)

        '''
        while i <= f:
            if int(colecao[i]['weight']) <= int(pivo['weight']):
                i+=1
            elif int(pivo['weight']) < int(colecao[f]['weight']):
                f-=1
            else:
                troca = colecao[i]
                colecao[i] = colecao[f]
                colecao[f] = troca
                i+=1
                f-=1
        colecao[inicio] = colecao[f]
        colecao[f] = pivo
        
        return f
        '''

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
