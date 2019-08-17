class Fila(object):
    def __init__(self):
        self.dados = []

    def insert(self, elemento):
        self.dados.append(elemento)
    
    def remove(self):
        return self.dados.pop(0)
    
    def len():
        return len(self.dados)

class NoGrafo: #tratamento como lista
    def __init__(self, vizinhos):
        self.vizinhos = vizinhos
    
    def novoVizinho(self, vizinho):
        self.vizinhos.append(vizinho)

    def removeVizinho(self, vizinho):
        self.vizinho.pop(vizinho)

class Grafo:

    def __init__(self, node):
        self.nodes = []
        self.dist = []
        self.marcado = []
        self.nodes.append(node)
        self.marcado.append(False)
        self.qtd_vertices = 1
    
    def adicionaNode(self, node):
        self.nodes.append(node)
        self.dist.append(0) #armazena o valor
        self.marcado.append(False) #define que não está marcado
        self.qtd_vertices+=1
    
    def buscaProfundidade(self, start):
        self.marcado[start-1] = True
        for i in range(len(self.nodes)):
            for v in self.nodes[start-1].vizinhos:
                w = v
                if not self.marcado[w-1]:
                    print(" " + str(w))
                    self.buscaProfundidade(w)
        self.cleanMarcados()
    
    def buscaLargura(self, start): 
        listavert = []
        f = Fila()
        self.marcado[start-1] = True
        self.dist[start-1] = 0
        f.insert(start)
        while f.len > 0:
            vert = f.remove()
            for i in range(1, len(self.nodes)+1):
                listavert = self.nodes[vert-1].vizinhos #pega a lista de vizinhos
                for j in range(0, len(listavert)):
                    w = listavert[j]
                    if not self.marcado[w-1]:
                        self.marcado[w-1] = True
                        self.dist[w-1] = dist[vert-1]+1
                        f.insert(w)
        self.zerarDist()

    def cleanMarcados(self):
        for m in self.marcado:
            m = False
    
    def zerarDist(self):
        for d in self.dist:
            d = 0

'''<<<<<<<<<<<<<------------- Main Code ---------------------->>>>>>>>>>>>>>'''
n1 = NoGrafo([5,4,3,2])
n2 = NoGrafo([3,1])
n3 = NoGrafo([4,2,1])
n4 = NoGrafo([5,3,1])
n5 = NoGrafo([4,1])

g = Grafo(n1)
g.adicionaNode(n2)
g.adicionaNode(n3)
g.adicionaNode(n4)
g.adicionaNode(n5)

g.buscaProfundidade(1)