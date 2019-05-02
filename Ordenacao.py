import random

def SelectionSort(v):
    for i in range(0, len(v)-1):
        m = i
        for j in range(i, len(v)):
            if v[j] < v[m]:
                m = j
        
        temp = v[m]
        v[m] = v[i]
        v[i] = temp
    
    return v

def InsertionSort(v):
    for j in range(1, len(v)):
        chave = v[j]
        i = j-1
        while i>=0 and v[i] > chave:
            v[i+1] = v[i]
            i-=1
        v[i+1] = chave
    
    return v

def ShellSort(v):
    h = 1
    for h in range(1, len(v), 3*h+1):
        while h > 0:
            h = int((h-1)/3)
            for i in range(h, len(v)):
                temp = v[i]
                j = i

                while v[j-h] > temp:
                    v[j] = v[j-h]
                    j = j -h
                    if j < h: 
                        break
                v[j] = temp

    return v

#incio do MergeSort

def MergeSort(v): 
    if len(v) >1: 
        mid = len(v)//2
        L = v[:mid]  
        R = v[mid:]  
  
        MergeSort(L) 
        MergeSort(R)
  
        i = j = k = 0
        
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                v[k] = L[i] 
                i+=1
            else: 
                v[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            v[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            v[k] = R[j] 
            j+=1
            k+=1
    
#fim do MergeSort

#Inicio do QuickSort
def QuickSort(v, inicio, fim):
    if inicio < fim:
        posicaoPivo = Particiona(v, inicio, fim)

        QuickSort(v, inicio, posicaoPivo - 1)
        QuickSort(v, posicaoPivo + 1, fim)

def Particiona(v, inicio, fim):
    pivo = v[inicio]
    i = inicio +1
    f = fim

    while i <= f:
        if v[i] <= pivo:
            i+=1
        elif pivo < v[f]:
            f-=1
        else:
            troca = v[i]
            v[i] = v[f]
            v[f] = troca
            i+=1
            f-=1
    v[inicio] = v[f]
    v[f] = pivo

    return f

#fim do QuickSort

#inicio HeapSort
def HeapSort(v):
    n = len(v)

    #construindo MaxHeap
    for i in range(n, -1, -1):
        Heapify(v, n, i)
    
    #extrair um a um os elementos
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i] #troca
        Heapify(v, i, 0)

def Heapify(v, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and v[i] < v[l]:
        largest = l
    
    if r < n and v[largest] < v[r]:
        largest = r
    
    if largest != i:
        v[i], v[largest] = v[largest], v[i]

        Heapify(v, n, largest)

#fim do HeapSort

def CountSort(v):
    max_value = min_value = v[0]
    for num in v:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    ran = max_value - min_value + 1
    count = [0]*ran
    output = [0]*len(v)
    for i in range(0, len(v)):
        count[v[i] - min_value]+=1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(v)-1, -1, -1):
        output[count[v[i] - min_value] - 1] = v[i]
        count[v[i] - min_value]-=1
    for i in range(0, len(v)):
        v[i] = output[i]

def createVector():
    n = 100
    vet = []
    for i in range(n):
        vet.append(random.randint(1,n+1))
    
    return vet

def teste():
    for i in range(0, 7):
        vet = createVector()
        print(vet)
        print()
        if i == 0:
            print("SelectionSort")
            SelectionSort(vet)
        if i == 1:
            print("InsertionSort")
            InsertionSort(vet)
        if i == 2:
            print("ShellSort")
            ShellSort(vet)
        if i == 3:
            print("MergeSort")
            MergeSort(vet)
        if i == 4:
            print("QuickSort")
            QuickSort(vet, 0, len(vet)-1)
        if i == 5:
            print("HeapSort")
            HeapSort(vet)
        if i == 6:
            print("CountSort")
            CountSort(vet)
        print()
        print(vet)
        print()
        print()

#teste()