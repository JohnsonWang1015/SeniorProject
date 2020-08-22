/*
�Z��:105
�y��:2
�m�W:������
�D��:����ֳz�︹�� 
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void Repeat(int Lotto,int Num){
	int n,temp;
	int lotto[Lotto];
	srand(time(NULL)); //�üƲ���
	for(int i=1; i<=Lotto; i++) //��J49�Ӹ��X
		lotto[i]=i;
	for(int i=1; i<=Num; i++) {  //49�ӿ�X6�Ӹ��X�洫
		n=rand()%Lotto+1;
		temp=lotto[n];
		lotto[n]=lotto[i];
		lotto[i]=temp;
	}
	for(int i=1; i<=Num; i++) { //�洫-->�Ѥp�ƨ�j(if�O�p��)
		for(int j=1; j<i; j++) {
			if(lotto[i]<lotto[j]) {
				temp=lotto[j];
				lotto[j]=lotto[i];
				lotto[i]=temp;
			}
		}
	}
	
	for(int i=1;i<=Num;i++){
		printf("%d ",lotto[i]);
	}
}


int main() {
	int keyin;
	do {
		printf("\n\n�п�� 1)�j�ֳz 2)�¤O�m 3)���m539 4)�j�ֱm 5)�����G");
		scanf("%d",&keyin);
		switch(keyin) {
			case 1:
				Repeat(49,6);
				printf("  ");
				Repeat(49,1); 
				break;
			case 2:
				Repeat(38,8);
				printf("  ");
				Repeat(38,1);
				break;
			case 3:
				Repeat(39,5);
				printf("  ");
				Repeat(39,1);
				break;
			case 4:
				Repeat(40,7);
				printf("  ");
				Repeat(40,1);
				break;
			case 5:
				printf("----OVER----");
				break;
			default:
				printf("��J���~�A�ЦA��J�@��");
				continue;
		}
		if(keyin==5){
			break;
		}
	} while(true);
	
	system("pause");
	return 0;
}
