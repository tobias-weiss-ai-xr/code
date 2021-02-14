/* aufg0037.c */
#include <stdio.h>

int main(void){
    char satz[100];
    int i=0;
    printf("Bitte geben sie einen Satz ein: ");
    fgets(satz,100,stdin);
    while(satz[i]){
	if(satz[i]==' '){
	    printf("\n");
	} else
	    printf("%c",satz[i]);
	    i++;
    }
    return 0;
}
