/* aufg0034.c */
#include <stdio.h>
#include <string.h>

int main(void){
    char str[100];
    size_t length;
    int i=0,count=0;
    float perc;

    printf("Bitte geben Sie einen str mit maximal 100 Woertern ein: ");
    fgets(str,100,stdin);
    printf("Ihre Eingabe lautete: %s",str);
    length = strlen(str);
    printf("Der str hat %i Zeichen - ohne \\n und \\0\n",length-1); 
    while(str[i]){
	if(str[i++]=='e') count++;
    }
    perc = 100.0/(length-1)*count;
    printf("Die Anzahl der e's betraegt %i.\n",count);
    printf("Dies entspricht %.0f Prozent.\n",perc);
    return 0;
}
