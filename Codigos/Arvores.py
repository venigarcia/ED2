import Ordenacao as sort
import random
import math
import sys

sys.setrecursionlimit(15000)

class ArvoreAVL:
    #self.dado = None
    #self.pai = None
    #self.esq = None
    #self.dir = None

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
    
    def insere(self, dado):
        if dado <= self.dado:
            if not self.esq:
                self.esq = ArvoreAVL(dado)
            else:
                self.esq.insere(dado)
        else:
            if not self.dir:
                self.dir = ArvoreAVL(dado)
            else:
                self.dir.insere(dado)
        self.balancear()
    
    def imprimeArvore(self, indent = 0):
        print(" " + indent + str(self.dado))
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

    def insere(self, dado):
        nodePai = self
        createdNode = None
        if dado <= self.dado:
            if not self.esq:
                self.esq = ArvoreRubroNegra(dado, pai=nodePai)
                createdNode = self.esq
            else:
                self.esq.insere(dado)
        else:
            if not self.dir:
                self.dir = ArvoreRubroNegra(dado, pai=nodePai)
                createdNode = self.dir
            else:
                self.dir.insere(dado)
        if createdNode != None:
            createdNode.colorir()
    
    def imprimeArvore(self, indent = 0):
        print(" " * indent + str(self.dado) + ' - ' + self.cor)
        if self.esq:
            self.esq.imprimeArvore(indent + 2)
        if self.dir:
            self.dir.imprimeArvore(indent + 2)

class ArvoreB:

    self.ordem = None

    def __init__(self, ordem=None): #cria uma página para a árvore
        self.totalChaves = 0 #armazena o total de chaves da página
        self.chaves = [] #armazena as chaves da árvore
        self.filhos = [] #armazena os filhos
        if self.ordem is None:
            self.ordem = ordem

    def isFolha(self):
        if len(filhos) == 0:
            return True
        else:
            return False
    
    def buscaChave(self, chave):
        if chave in self.chaves:
            return self
        i = 0
        while i < self.totalChaves and chave > self.chaves[i]:
            i+=1
        if i < self.totalChaves and chave == self.chaves[i]:
            return self
        if self.isFolha():
            return None
        else:
            return buscaPag(self.filhos[i], k)


    def inserir(self, chave, chavePromovida=None):
        '''
            chave: chave que será inserida na árvore
            chavePromovida: a chave que será realocado depois da realização de um split
        '''
        localInsert = self.buscaChave(chave) #busca a página a onde a chave deveria estar contida
        if localInsert is None:
            #verifica se está vázio
            if self.totalChaves == 0:
                self.chaves[self.totalChaves] = chave
                self.totalChaves+=1
            else:
                if(self.totalChaves == self.ordem):
                    s = ArvoreB()
                    s.filhos.append(self)
                    s.split(0, r)
                    s.insereNaoCheio(chave)
                    return s #tratar o caso de a raiz mudar, pois a árvore b só cresce a partir do split
                else:
                    self.insereNaoCheio(chave)
            return None
    
    def insereNaoCheio(self, chave):
        i = self.totalChaves

        if self.isFolha():
            self.chaves.add(chave).sort()
            self.totalChaves+=1
        else:
            while i>=0 and chave < self.chaves[i]:
                i-=1
            i+=1
            if self.filhos[i].totalChaves == ordem:
                self.split(i, self.filhos[i])
                if chave > self.chaves[i]:
                    i+=1
            self.filhos[i].insereNaoCheio(chave)    
            
    def split(self, i, y):
        dif = 1
        t = int(math.floor((self.ordem-1)/2))
        z = ArvoreB()
        z.totalChaves = t
        if (self.ordem-1) % 2 == 0: #verifica se é par
            dif = 0  
        for e in y.chaves[t+dif:]: #pega os t ultimos elemetos e coloca na lista de chaves
            z.chaves.append(e) 
            y.totalChaves-=1
        if not y.isFolha(): #se não for folha 
            for f in y.filhos[t+dif:]: #transfere os t útlimos filhos para o novo nó
                z.filhos.append(f)      
        y.totalChaves = t #nova quantidade de chaves de 
        self.filhos.insert(i+1, z)
        self.chaves 
        self.chaves.insert(i, y.chaves[t+(dif-1)])
        y.totalChaves-=1
        self.totalChaves+=1

    def remove(self, chave):
        node = self.buscaChave(chave)
        if not node is None:
            i = 0
        while node.chaves[i] < chave:
            i+=1

        if node.isFolha():
            del node.chaves[i]
            node.totalChaves-=1
            if node != self:
                balancear()
        else:
            ante = self.antecessor(chave)
            y = ante.chaves[ante.totalChaves-1]
            ante.totalChaves = ante.totalChaves -1
            node.chaves[i] = y
            ante.balancear()

    def balancear(): #balanceia_folha()
        if self.totalChaves < math.floor((self.ordem-1)/2):
            pai = self.getPai()
            j = 0
            while pai.filhos[j] not is self:
                j+=1
            if j == 0 or pai.filhos[j-1].totalChaves == math.floor((self.ordem-1)/2):
                if j == pai.totalChaves + 1 or pai.filhos[j].totalChaves == math.floor((self.ordem-1)/2):
                    self.diminui_altura()
                else:
                    pai.balancear_dir_esq(j, pai.filhos[j+1], self)
            else:
                pai.balancear_esq_dir(j-1, pai.filhos[j-1], self)
    
    def podar(): #diminui_altura()
    
    
    def balancear_esq_dir():

    def balancear_dir_esq():
    
    def mergeNode():

    def antecessor():

    


    


        
    



#v = [1, 4, 3, 5, 6, 7]
#a = ArvoreRubroNegra(2)
v = [2, 14, 1, 7, 13, 15, 5, 8, 4]
a = ArvoreRubroNegra(11)
for value in v:
    print(value)
    a.insere(value)
    a.imprimeArvore()
    print('-'*15)