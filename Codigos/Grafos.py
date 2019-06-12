class NoGrafo: #tratamento como lista
    def __init__(self, id, vizinhos):
        self.id = id
        self.vizinhos = vizinhos

class Grafo:

    def __init__(self, node):
        self.nodes = []
        self.marcado = []
        self.nodes.append(node)
        self.marcado.append(False)
        self.qtd_vertices = 1
    
    def adicionaNode(self, node):
        self.nodes.append(node)
        self.marcado.append(False)
        self.qtd_vertices+=1
    
    def buscaProfundidade(self, start):
        self.marcado[start-1] = True
        for i in range(len(self.nodes)):
            for v in self.nodes[start].vizinhos:
                w = v.id
                if not self.marcado[w-1]:
                    print(" " + str(w))
                    self.buscaProfundidade(w)
        self.cleanMarcados()
    
    def cleanMarcados(self):
        for m in self.marcado:
            m = False


