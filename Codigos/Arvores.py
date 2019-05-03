import Ordenacao as sort
import random
import math

class Arvore:
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
                self.esq = Arvore(dado)
            else:
                self.esq.insere(dado)
        else:
            if not self.dir:
                self.dir = Arvore(dado)
            else:
                self.dir.insere(dado)
        self.balancear()
    
    def imprimeArvore(self, ident = 0):
        print " " + indent + str(self.dado)
        if self.esq:
            self.esq.imprimeArvore(indent + 2)
        if self.dir:
            self.dir.imprimeArvore(indent + 2)