/* aufg0036.c */
#include <stdio.h>
#include <string.h>

int main(void){
    char str[100],strn[100];
    int i=0,b=0;

    printf("Bitte str eingeben: ");
    fgets(str,100,stdin);
    while(str[i]){
	switch(str[i]){
	case '.':
	    break;
	default:
	printf("%c",str[i]); 
	}
    i++;
    }
    return 0; 
}
