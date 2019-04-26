import Ordenacao as sort

def busca_seq(vet, dado):
    for v in vet:
        if v == dado:
            return v
    
    return None

def busca_bin(vet, dado):
    ini = 0
    fim = len(vet) - 1
    meio = (ini + fim) / 2

    if vet[meio] == dado:
        return vet[meio]
    elif vet[meio] > meio:
        return busca_bin(vet[meio:fim], dado)
    else:
        return busca_bin(vet[ini:meio], dado)
    
def busca_hash():


def createVector():
    n = 100
    vet = []
    for i in range(n):
        vet.append(random.randint(1,n+1))
    
    return vet


vetor = createVector()
vetor = sort.InsertionSort()
a = busca_bin(vetor, 2)