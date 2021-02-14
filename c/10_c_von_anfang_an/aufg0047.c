 /* file: aufg0047.c
  * creator: TW
  * Last modified:  2015 Feb 19 23:40:11
  * Aufgabe: String nach einem Zeichen durchsuchen und dieses ersetzen!
  */

#include <stdio.h>
#include <string.h>

#define MAX_STRING 80

void replaceString(char *ptr, char *search, char *replace){
    do {	
	if(*ptr==*search){
	    *ptr=*replace;
	}
    } while(*ptr++);
}

int main(void)
{
  char e[MAX_STRING];
  char search,replace;
  printf("\nBitte einen String eingeben:");
  fgets(e, MAX_STRING, stdin);
  printf("\nBitte Suchzeichen eingeben:");
  search=fgetc(stdin);
  printf("\nBitte das Eresetzzeichen eingeben:");
  __fpurge(stdin);
  replace=fgetc(stdin);
  printf("\nDer String lautet: %s",e);
  printf("\nSearchstring: %c, Replacestring: %c",search,replace);
  replaceString(e,&search,&replace); 
  printf("\nDer neue String lautet: %s\n\n",e);
  return 0;
}

