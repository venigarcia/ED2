import random
import argparse
import codecs

PATH = "../Data/palavras.txt"

parser = argparse.ArgumentParser(description='Gera um arquivo com uma quantidade de palavras especificada, de forma aleatoria.')
parser.add_argument('--qtd_palavras', type=int, required=True, dest='qtd_palavras', help='Quantidade de palavras no arquivo')
parser.add_argument('--out_file', type=str, required=True, dest='arq', help='Arquivo de saida para as palavras selecionadas')

args = parser.parse_args()

if __name__ == "__main__":
    f = codecs.open(PATH, encoding='utf-8')
    words = f.readlines()
    f.close()
    output_words = []
    for i in range(args.qtd_palavras):
        output_words.append(words[random.randint(0, len(words)-1)])
    o = codecs.open("../Data/" + args.arq, encoding='utf-8', mode='w+')
    o.writelines(output_words)
    o.close()
    