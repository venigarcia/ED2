#include <iostream>

using namespace std;

void BubbleSort(int *vet, int vet_len){ //melhor desempenho, porém, apresenta outras variações de código.
	int n, i, aux, troca;
	n = 1;
	troca = 1;
	while(n <= vet_len && troca == 1){
		troca = 0;
		for(i=0;i<=vet_len-2;i++){ //como executa de 2 em 2, usa-se o tamanho do vetor menos 2, pois o laço deve percorrer até a penúltima posição do vetor
			if(vet[i] < vet[i+1]){
				troca=1;
				aux = vet[i];
				vet[i] = vet[i+1];
				vet[i+1] = aux;
			}
		}
		n++;
	}
}

void InsertionSort(int *vet, int vet_len){ //melhor desempenho
	int i, j, eleito;
	for(i=1;i<=vet_len-1;i++){
		eleito = vet[i];
		j = i - 1;
		//laço que percorre os elementos à esquerda
		//do número eleito, ou até encontrar a posição
		//para recolocação do número eleito
		//respeitando ordenação procurada
		while(j >= 0 && vet[j] > eleito){
			vet[j+1] = vet[j];
			j = j - 1;
		}
		vet[j+1] = eleito;
	}
}

void SelectionSort(int *vet, int vet_len){
	int i, j, eleito, menor, pos;
	//ordenando de forma crescente
	//laço que percorre da primeira a penultima posição
	for(i=0;i<=vet_len-2;i++){
		eleito = vet[i];
		//buscando o menor numero à direita do eleito, com sua posição
		menor = vet[i+1];
		pos = i+1;
		//laço que percorre os elementos à direita do eleito, buscando o menor dentre eles e sua posição
		for(j=i+1;j<=vet_len-1;j++){
			if(vet[j] < menor){
				menor = vet[j];
				pos = j;
			}
		}
		//troca o número eleito com o da posição pos, este é o menor número a direita do escolhido
		if(menor < eleito){
			vet[i] = vet[pos];
			vet[pos] = eleito;
		}
	}
}

void MergeSort(int *vet, int vet_len){
	//PAG 69 (PDF)
}

int main(){

}


