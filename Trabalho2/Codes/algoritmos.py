import sys

sys.setrecursionlimit(15000)

class Palavra:

    def __init__(self, word):
        self.order = int(''.join(str(ord(c)) for c in word))
        self.lexico = word
        self.ocorrencias = 1
    
    def __str__(self):
        return "Order: {} Lexico: {} Ocorrências: {}".format(self.order, self.lexico, self.ocorrencias)
    
    def comp_word(self, word):
        if self.lexico == word:
            return True
        else:
            return False
    
    def newAppear(self):
        self.ocorrencias+=1

class  HashTableDuplo:

    def __init__(self, vet):
        self.hash_table = [None] * len(vet)
        self.create_hash_duplo(vet)

    def busca_hash_duplo(self, dado):
        p = Palavra(dado)
        c1 = p.order + 37
        c2 = p.order + 31
        if c2 % 2 == 0:
            c2+=1
        k = 0
        while k <= len(self.hash_table)-1:
            chave = self.transform_hash(c1 + k*c2, len(self.hash_table))
            if self.hash_table[chave] == p.order:
                return self.hash_table[chave]
            k+=1
        return None
    
    def create_hash_duplo(self, vet): #cria o hash de endereçamento aberto de forma dupla, tem outros metódos de definir tal hash, como por exemplo c1 = (v % n) e c2 = (v % (n-1)) + 1 sendo n um número primo
        #essa abordagem se baseia na escolha de dois números primos, a sua escolha, contanto que o N de c1 seja menor e primo em relação a c2
        for v in vet:
            p = Palavra(v)
            c1 = p.order + 37
            c2 = p.order + 31
            if c2 % 2 == 0:
                c2+=1
            k = 0
            while k < len(vet):
                chave = self.transform_hash(c1 + k*c2, len(vet))
                if self.hash_table[chave] == None:
                    self.hash_table[chave] = p
                    break
                else:
                    e = self.hash_table[chave]
                    if e.comp_word(p.lexico):
                        e.newAppear()
                        break
                k+=1

    def transform_hash(self, dado, M):
        return dado % M

class HashTableEncad:

    def __init__(self, vet):
        self.hash_table = [None] * len(vet)
        self.create_hash_encad(vet)

    def create_hash_encad(self, vet):#cira o hash por encadeamento
        for v in vet:
            p = Palavra(v)
            chave = self.transform_hash(p.order, len(vet))
            if self.hash_table[chave] == None:
                self.hash_table[chave] = p
            else:
                if type(self.hash_table[chave]) is list:
                    inserted = False
                    for itens in self.hash_table[chave]:
                        e = itens
                        if e.comp_word(p.lexico):
                            e.newAppear() 
                            inserted = True
                            break
                    if not inserted:
                        self.hash_table[chave].append(p)
                else:
                    lista = []
                    lista.append(self.hash_table[chave])
                    lista.append(p)
                    self.hash_table[chave] = lista

    def busca_hash_encad(self, dado):
        p = Palavra(dado)
        chave = self.transform_hash(p.order, len(self.hash_table))
        if chave < len(self.hash_table):
            if type(self.hash_table[chave]) is list:
                for h in self.hash_table[chave]:
                    if h == dado:
                        return h
            else:
                if self.hash_table[chave] == dado:
                    return self.hash_table[chave]   
        return None
    
    def transform_hash(self, dado, M):
        return dado % M

class ArvoreAVL:

    def __init__(self, data):
        self.dado = data
        self.setaFilhos(None, None)
        self.setaPai(None)
    
    def setaFilhos(self, esquerda, direita):
        self.esq = esquerda
        self.dir = direita
    
    def setaPai(self, pai):
        self.pai = None
    
    def balanco(self): #calcula o balanceamento da árvore
        prof_esq = 0
        if self.esq:
            prof_esq = self.esq.profundidade()
        prof_dir = 0
        if self.dir:
            prof_dir = self.dir.profundidade()
        return prof_esq - prof_dir
    
    def profundidade(self):
        prof_esq = 0
        if self.esq:
            prof_esq = self.esq.profundidade()
        prof_dir = 0
        if self.dir:
            prof_dir = self.dir.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.dado, self.dir.dado = self.dir.dado, self.dado
        old_esq = self.esq
        self.setaFilhos(self.dir, self.dir.dir)
        self.esq.setaFilhos(old_esq, self.esq.esq)
    
    def rotacaoDireita(self):
        self.dado, self.esq.dado = self.esq.dado, self.dado
        old_dir = self.dir
        self.setaFilhos(self.esq.esq, self.esq)
        self.dir.setaFilhos(self.dir.dir, old_dir)

    def rotacaoEsqDir(self):
        self.esq.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDirEsq(self):
        self.dir.rotacaoDireita()
        self.rotacaoEsquerda()
    
    def balancear(self):
        bal = self.balanco()
        if bal > 1:
            if self.esq.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsqDir()
        elif bal < -1:
            if self.dir.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDirEsq()
    
    def buscar(self, dado):
        dado = Palavra(dado)
        if dado.order == self.dado.order:
            return self.dado
        elif dado.order < self.dado.order:
            if self.esq:
                return self.esq.buscar(dado.lexico)
            return None
        else:
            if self.dir:
                return self.dir.buscar(dado.lexico)
            return None
    
    def insere(self, dado):
        dado = Palavra(dado)
        exist = self.buscar(dado.lexico)
        if exist:
            exist.newAppear()
        else:
            if dado.order <= self.dado.order:
                if not self.esq:
                    self.esq = ArvoreAVL(dado)
                else:
                    self.esq.insere(dado.lexico)
            else:
                if not self.dir:
                    self.dir = ArvoreAVL(dado)
                else:
                    self.dir.insere(dado.lexico)
            self.balancear()

    def imprimeArvore(self, indent = 0):
        print(" " * indent + str(self.dado))
        if self.esq:
            self.esq.imprimeArvore(indent + 2)
        if self.dir:
            self.dir.imprimeArvore(indent + 2)

class ArvoreRubroNegra:
    #cor='p' -> nó preto
    #cor='r' -> nó vermelho
    
    def __init__(self, data, pai=None, cor='v'):
        self.dado = data
        self.cor = cor
        self.setaFilhos(None, None)
        self.setaPai(pai)
        if pai == None:
            self.colorir()

    def setaFilhos(self, esquerda, direita):
        self.esq = esquerda
        self.dir = direita
    
    def setaPai(self, pai):
        self.pai = pai
    
    def rotacaoEsquerda(self):
        self.dado, self.dir.dado = self.dir.dado, self.dado
        self.cor, self.dir.cor = self.dir.cor, self.cor
        old_esq = self.esq
        self.setaFilhos(self.dir, self.dir.dir)
        self.esq.setaFilhos(old_esq, self.esq.esq)

    def rotacaoDireita(self):
        self.dado, self.esq.dado = self.esq.dado, self.dado
        self.cor, self.esq.cor = self.esq.cor, self.cor
        old_dir = self.dir
        self.setaFilhos(self.esq.esq, self.esq)
        self.dir.setaFilhos(self.dir.dir, old_dir)
        
    def tio(self):
        if self.dado > self.pai.pai.dado:
            return self.pai.pai.esq
        else:
            return self.pai.pai.dir

    def colorir(self):
        if self.pai == None:
            self.cor = 'p'
        else:
            if self.pai.cor == 'p':
                return
            if self.tio().cor == 'v':
                self.pai.cor = 'p'
                self.tio().cor = 'p'
                self.pai.pai.cor = 'v'
                self.pai.pai.colorir()
            else:
                if self.dado > self.pai.dado and self.dado <= self.pai.pai.dado:
                    self.pai.rotacaoEsquerda()
                    n = self.esq
                else:
                    self.pai.rotacaoDireita()
                    n = self.dir
                n.pai.cor = 'p'
                n.pai.pai.cor = 'v'
                if n.dado <= n.pai.dado and n.dado <= n.pai.pai.dado:
                    n.pai.pai.rotacaoDireita()
                else:
                    n.pai.pai.rotacaoEsquerda()

    def buscar(self, dado):
        dado = Palavra(dado)
        if dado.order == self.dado.order:
            return self.dado
        elif dado.order < self.dado.order:
            if self.esq:
                return self.esq.buscar(dado.lexico)
            return None
        else:
            if self.dir:
                return self.dir.buscar(dado.lexico)
            return None

    def insere(self, dado):
        dado = Palavra(dado)
        nodePai = self
        createdNode = None
        exist = self.buscar(dado.lexico)
        if exist:
            exist.newAppear()
        else:        
            if dado.order <= self.dado.order:
                if not self.esq:
                    self.esq = ArvoreRubroNegra(dado, pai=nodePai)
                    createdNode = self.esq
                else:
                    self.esq.insere(dado.lexico)
            else:
                if not self.dir:
                    self.dir = ArvoreRubroNegra(dado, pai=nodePai)
                    createdNode = self.dir
                else:
                    self.dir.insere(dado.lexico)
            if createdNode != None:
                createdNode.colorir()
    
    def imprimeArvore(self, indent = 0):
        print(" " * indent + str(self.dado) + ' - ' + self.cor)
        if self.esq:
            self.esq.imprimeArvore(indent + 2)
        if self.dir:
            self.dir.imprimeArvore(indent + 2)
    