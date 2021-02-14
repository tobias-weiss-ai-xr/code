/* aufg0023.c */
#include <stdio.h>

int main(void)
{
  double wert,minderung,rest;
  int jahr=1;
  printf("\n\tWertminderung\n");
  printf("\nWert\t\t: ");
  scanf("%lf",&wert);
  printf("\n%% Wertminderung\t: ");
  scanf("%lf",&minderung);
  printf("\nRestwert\t\t: ");
  scanf("%lf",&rest);
  while(wert>rest){
    wert=wert*((100-minderung)/100);
    printf("\n Wert nach %2i Jahren %7.2f.\n",jahr,wert);
    jahr=jahr+1;
  } 
  return 0;
}


