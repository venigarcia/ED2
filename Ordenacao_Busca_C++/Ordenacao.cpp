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

void intercala(int *vet, int vet_len, int inicio, int fim, int meio){
	int poslivre, inicio_vet1, inicio_vet2, i;
	int aux[vet_len];
	inicio_vet1 = inicio;
	inicio_vet2 = meio + 1;
	poslivre = inicio;
	while(inicio_vet1 <= meio && inicio_vet2 <= fim){
		if(vet[inicio_vet1] <= vet[inicio_vet2]){
			aux[poslivre] = vet[inicio_vet1];
			inicio_vet1++;
		}else{
			aux[poslivre] = vet[inicio_vet2];
			inicio_vet2++;
		}
		poslivre++;
	}
	//se ainda existem números no primeiro vetor que não foram intercalados
	for(i=inicio_vet1;i<=meio;i++){
		aux[poslivre] = vet[i];
		poslivre++;
	}
	//se ainda existem números no segundo vetor que não foram intercalados
	for(i=inicio_vet2;i<=fim;i++){
		aux[poslivre] = vet[i];
		poslivre++;
	}
	//retorna os valores do vetor aux para o vetor X
	for(i=inicio;i<=fim;i++)
		vet[i] = aux[i];
}

void MergeSort(int *vet, int vet_len, int inicio, int fim){
	int meio;
	if(inicio < fim){
		meio = (inicio+fim)/2;
		MergeSort(vet, vet_len, inicio, meio);
		MergeSort(vet, vet_len, meio+1, fim);
		intercala(vet, vet_len, inicio, fim, meio);
	}
}

void troca(int *vet, int i, int j){
	int aux;
	aux = vet[i];
	vet[i] = vet[j];
	vet[j] = aux;
}

int particao(int *vet, int p, int r){
	int pivo, i, j;
	pivo = vet[(p+r)/2];
	i = p-1;
	j = r+1;
	while(i < j){
		do{
			j--;
		}while(vet[j] > pivo);
		do{
			i++;
		}while(vet[i] < pivo);
		if(i<j) troca(vet, i, j);
	}
	return j;
}

void QuickSort(int *vet, int vet_len, int p, int r){
	int q;
	if(p < r){
		q = particao(vet, p, r);
		QuickSort(vet, vet_len, p, q);
		QuickSort(vet, vet_len, q+1, r);
	}
}

//Heap Sort
void heap_fica(int *vet, int i, int qtde){ //qtde corresponde o tamanho do vetor
	int f_esq,  f_dir, maior, aux;
	maior = i;
	if(2*i+1 <= qtde){
		//o nó que está sendo analisado tem filhos a esquerda e direita
		f_esq = 2*i+1;
		f_dir = 2*i;
		if(vet[f_esq] >= vet[f_dir] && vet[f_esq] > vet[i])
			maior = 2*i+1;
		else if(vet[f_dir] > vet[f_esq] && vet[f_dir] > vet[i])
			maior = 2*i;
	} else if(2*i <= qtde){
		// o nó que está sendo analisado tem filhos apenas para a direita
		f_dir = 2*i;
		if(vet[f_dir] > vet[i]){
			maior = 2*i;
		}
		if(maior != i){
			aux = vet[i];
			vet[i] = vet[maior];
			vet[maior] = aux;
			heap_fica(vet, maior, qtde);
		}
	}
}

void transforma_heap(int *vet, int qtde){
	int i, pai, aux;
	for(i=qtde/2;i>=2;i--){
		heap_fica(vet, i, qtde);
	}
}

void ordena(int *vet, int qtde){
	int i, aux, ultima_posi;
	for(i=qtde/2;i>=2;i--){
		aux = vet[1];
		vet[1] = vet[i];
		vet[i] = aux;
		ultima_posi = i-1;
		heap_fica(vet, 1, ultima_posi);
	}
}


int main(){

}


