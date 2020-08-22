/*
班級:105
座號:2
姓名:王嘉暐
題目:完整樂透選號器 
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void Repeat(int Lotto,int Num){
	int n,temp;
	int lotto[Lotto];
	srand(time(NULL)); //亂數產生
	for(int i=1; i<=Lotto; i++) //填入49個號碼
		lotto[i]=i;
	for(int i=1; i<=Num; i++) {  //49個選出6個號碼交換
		n=rand()%Lotto+1;
		temp=lotto[n];
		lotto[n]=lotto[i];
		lotto[i]=temp;
	}
	for(int i=1; i<=Num; i++) { //交換-->由小排到大(if是小於)
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
		printf("\n\n請選擇 1)大樂透 2)威力彩 3)今彩539 4)大福彩 5)結束：");
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
				printf("輸入錯誤，請再輸入一次");
				continue;
		}
		if(keyin==5){
			break;
		}
	} while(true);
	
	system("pause");
	return 0;
}
