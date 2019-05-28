import math

class Arvore:
    ordem = 5
    qtdChaves = 0
    chaves = []
    filhos = []

    def split(self, i, y):
        dif = 1
        t = int(math.floor((self.ordem-1)/2))
        z = Arvore()
        z.qtdChaves = t #atenção aqui, deve definir o máximo de elementos presentes na arvore
        if (self.ordem-1) % 2 == 0: #verifica se é par
            dif = 0  
        for e in y.chaves[t+dif:]: #pega os t ultimos elemetos e coloca na lista de chaves
            z.chaves.append(e) 
            y.qtdChaves-=1
        if not y.isFolha(): #se não for folha 
            for f in y.filhos[t+dif:]: #transfere os t útlimos filhos para o novo nó
                z.filhos.append(f)      
        y.qtdChaves = t #nova quantidade de chaves de 
        self.filhos.insert(i+1, z)
        self.chaves 
        self.chaves.insert(i, y.chaves[t+(dif-1)])
        y.qtdChaves-=1
        self.qtdChaves+=1       


