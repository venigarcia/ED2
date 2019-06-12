import argparse
from algoritmos import *
import cProfile, pstats, io
import codecs
import json

parser = argparse.ArgumentParser(description='Ordenar os nodes do grafo gerado.')
parser.add_argument('--arquivo', type=str, required=True, dest='arq', help='Caminho para o dicionario de palavras')
parser.add_argument('--saida', type=str, dest='save', help='Caminho para salvar o arquivo de Log da execução')
parser.add_argument('--hashencad', dest='encad', action='store_true', help='Estrutura de Hash Encadeado')
parser.add_argument('--hashduplo', dest='duplo', action='store_true', help='Estrutura de Hash Duplo')
parser.add_argument('--avl', dest='avl', action='store_true', help='Estrutura de árvore do tipo AVL')
parser.add_argument('--redblack', dest='redblack', action='store_true', help='Estrutura de árvore do tipo Red Black')

args = parser.parse_args()

path = "C:\\Users\\Desktop\\Documents\\GitHub\\ED2\\Trabalho2\\Data\\5000words.txt"

if __name__ == "__main__":
    if args.encad:
        estrutura = HashTableEncad()
    elif args.duplo:
        estrutura = HashTableDuplo()
    elif args.avl:
        estrutura = AvoreAVL()
    elif args.redblack:
        estrutura = ArvoreRubroNegra()

    '''arquivoJson = args.arq
    arquivoDeSaida = args.save
    print()
    print(arquivoDeSaida)
    print()
    for i in range(len(arquivoDeSaida)-6, -1, -1):
        if arquivoDeSaida[i] == '\\':
            break
    logFile = arquivoDeSaida[-(len(arquivoDeSaida)-1-i):-4]
    '''
    #algo = []
    #algos = [HashTableEncad(), HashTableDuplo(), AvoreAVL(), ArvoreRubroNegra()]
    #final_val = []
    #for algo in algos:     
    pr = cProfile.Profile()
    pr.enable()
    
    f = codecs.open(path, encoding='utf-8')
    words = f.readlines()
    f.close()
    
    a = ArvoreAVL(Palavra(words[0]))
    for w in words[1:]:
        a.insere(w)
        
    a.imprimeArvore()

    pr.disable()
    s = io.StringIO()

    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()
    

    out = s.getvalue()
    count = 0
    start = 0
    end = 0
    for i in range(9, len(out)):
        if out[i] == ' ':
            count+=1
        if count == 4 and start == 0:
            start = i+1
        if count == 5 and end == 0:
            end = i
            break
    #val=float(out[start:end])
    print(out)
    #print(val)
    #final_val.append(val)

    #final_dict = {"HashEncad":final_val[0], "HashDuplo":final_val[1], "AVL":final_val[2], "RedBlack":final_val[3]}
    #with open("../LogFiles/" + logFile + ".json", 'w+') as f:
    #    json.dump(final_dict, f)