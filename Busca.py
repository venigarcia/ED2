import Ordenacao as sort
import random

def busca_seq(vet, dado):
    for v in vet:
        if v == dado:
            return v
    
    return None

#busca binária possui duas abordagens, iterativa e recursiva
def busca_bin_recu(vet, dado):
    ini = 0
    fim = len(vet) - 1
    if len(vet) > 1:
        meio = int((ini + fim) / 2)
        if vet[meio] == dado:
            return vet[meio]
        elif vet[meio] > dado:
            return busca_bin_recu(vet[ini:meio], dado)
        else:
            return busca_bin_recu(vet[meio+1:fim+1], dado)
    
    return None

#tabela hash por open adreesing e listas lineares
def transform_hash(dado, M):
    return dado % M 

def create_hash_liner(vet):
    hash_table = [None] * len(vet)
    for v in vet:
        chave = transform_hash(v, len(vet))
        if hash_table[chave] == None:
            hash_table[chave] = v
        else:
            if type(hash_table[chave]) is list:
                hash_table[chave].append(v)
            else:
                lista = []
                lista.append(hash_table[chave])
                lista.append(v)
                hash_table[chave] = lista
    return hash_table        

def create_hash_open(vet):
    hash_table = [None] * len(vet)
    for v in vet:
        j = 0
        chave = v
        while j < len(vet):
            print("Chave: " + str(chave))
            print("Iter :" +str(j))
            print(len(vet))
            chave = transform_hash(chave+j, len(vet))
            print(chave)
            #print(str(v) + " " + str(chave))
            if hash_table[chave] == None:
                hash_table[chave] = v
                break
            j+=1
    return hash_table

def busca_hash_linear(hash_table, dado):
    chave = transform_hash(dado, len(hash_table))
    if chave < len(hash_table):
        if type(hash_table[chave]) is list:
            for h in hash_table[chave]:
                if h == dado:
                    return h
        else:
            if hash_table[chave] == dado:
                return hash_table[chave]   
    return None

def busca_hash_open(hash_table, dado):
    j = 0
    while j <= len(hash_table):
        chave = transform_hash(dado + j, len(hash_table))
        if hash_table[chave] == dado:
            return hash_table[chave]
        j+=1
    return None
    
def createVector():
    n = 10
    vet = []
    for i in range(n):
        vet.append(random.randint(1,n+1))

    return vet

vetor = createVector()
print(vetor)

hash_table = create_hash_open(vetor)

print(hash_table)

busc = 2
a = busca_hash_open(hash_table, busc)

print("Buscado: " + str(busc))
if a != None:
    print("Encontrado: " + str(a))
else:
    print("Não encontrado")