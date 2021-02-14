 /* file: aufg0046.c
  * creator: TW
  * Last modified:  2015 Feb 19 21:51:43
  */

#include <stdio.h>

void tausche(char *ptr1, char *ptr2){
  char *hilf;
  hilf=ptr1;
  ptr1=ptr2;
  ptr2=hilf;
}

int main(void)
{
  char e1[80];
  char e2[80];
  printf("\nBitte geben Sie eine Zeichenkette mit max. 80 Zeichen ein.");
  gets(e1);
  printf("\nBitte geben Sie eine zweite Zeichenkette mit max. 80 Zeichen ein.");
  gets(e2);
  printf("\nDie Eingabe lautete: '%s' und '%s'",e1,e2);
  tausche(&e1,&e2);
  printf("\nDie Eingabe lautet nach dem Tausch: '%s' und '%s'",e1,e2);
  return 0;
}

