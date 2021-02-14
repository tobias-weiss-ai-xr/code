/* aufg0039.c */
#include <stdio.h>

int naechste_zahl(void){
    static int i = 10;
    if(i > 12)
	i = 10;
    i++;
    return i;
}

int main(void){
    int x=1;
    while(x<10){
	printf("%4i",naechste_zahl());
	x++;
    }
	printf("\n");
    return 0;
}
