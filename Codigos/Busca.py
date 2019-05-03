import Ordenacao as sort
import random
import math

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

def create_hash_encad(vet):#cira o hash por encadeamento
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

def busca_hash_encad(hash_table, dado):
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

def create_hash_open(vet): #cria o hash de endereçamento aberto, por tentativa linear
    hash_table = [None] * len(vet)
    for v in vet:
        j = 0
        while j < len(vet)-1:
            chave = transform_hash(v+j, len(vet))
            if hash_table[chave] == None:
                hash_table[chave] = v
                break
            j+=1
    return hash_table

def busca_hash_open(hash_table, dado):
    j = 0
    while j <= len(hash_table)-1:
        chave = transform_hash(dado + j, len(hash_table))
        if hash_table[chave] == dado:
            return hash_table[chave]
        j+=1
    return None

def create_hash_open_quadratico(vet): #cria o hash de endereçamento aberto da forma quadrática
    hash_table = [None] * len(vet)
    for v in vet:
        k = 0
        chave = v
        while k < len(vet):
            chave = transform_hash(chave+k, len(vet))
            if hash_table[chave] == None:
                hash_table[chave] = v
                break
            k+=1
    return hash_table

def busca_hash_open_quadratico(hash_table, dado):
    k = 0
    chave = dado
    while k <= len(hash_table)-1:
        chave = transform_hash(chave + k, len(hash_table))
        if hash_table[chave] == dado:
            return hash_table[chave]
        k+=1
    return None

def create_hash_duplo(vet): #cria o hash de endereçamento aberto de forma dupla, tem outros metódos de definir tal hash, como por exemplo c1 = (v % n) e c2 = (v % (n-1)) + 1 sendo n um número primo
    hash_table = [None] * len(vet) #essa abordagem se baseia na escolha de dois números primos, a sua escolha, contanto que o N de c1 seja menor e primo em relação a c2
    for v in vet:
        c1 = v + 37
        c2 = v + 31
        if c2 % 2 == 0:
            c2+=1
        k = 0
        while k < len(vet):
            chave = transform_hash(c1 + k*c2, len(vet))
            if hash_table[chave] == None:
                hash_table[chave] = v
                break
            k+=1
    return hash_table

def busca_hash_duplo(hash_table, dado):
    c1 = dado + 37
    c2 = dado + 31
    if c2 % 2 == 0:
        c2+=1
    k = 0
    while k <= len(hash_table)-1:
        chave = transform_hash(c1 + k*c2, len(hash_table))
        if hash_table[chave] == dado:
            return hash_table[chave]
        k+=1
    return None
    
def createVector():
    n = 10
    vet = []
    for i in range(n):
        vet.append(random.randint(1,n+1))

    return vet

vetor = createVector()
print(vetor)

hash_table = create_hash_encad_interno(vetor)

print(hash_table)
print(len(hash_table))

busc = 2
a = busca_hash_encad_interno(hash_table, busc)

print("Buscado: " + str(busc))
if a != None:
    print("Encontrado: " + str(a))
else:
    print("Não encontrado")