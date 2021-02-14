 /* file: aufgabe003.c
  * creator: TW
  * Last modified:  2014 Sep 16 06:02:20
  */

#include <stdio.h>

int main(void)
{
  int zahl;
  float erg,rund; 
  printf("Bitte Zahl eingeben: ");
  scanf("%d", &zahl);
  erg = zahl;
  rund = erg - zahl;
  
  printf("zahl: %i\n",zahl);
  printf("erg: %f\n",erg);
  printf("rundungsfehler: %f\n",erg-zahl);
  return 0;
}

