/* bspl0015.c */
#include <stdio.h>

int main(void){
  int wahl;
  float betrag;
  printf("\b\t\tEUROUMRECHNER\n");
  printf("\n1. DM --> EURO\n2. EURO --> DM");
  printf("\nIhre Wahl?:");
  scanf("%i",&wahl);
  if (wahl == 1){
    printf("\nBitte DM-Betrag eingeben: ");
    scanf("%f",&betrag);
    printf("%.2f DM sind %.2f EURO\n",betrag,betrag*2);
  } else if (wahl == 2){
    printf("\nBitte EURO-Betrag eingeben: ");
    scanf("%f",&betrag);
    printf("%.2f EURO sind %.2f DM\n",betrag,betrag/2);
  } else
   printf("\nUngueltige Operation!\n");
  return 0;
}
