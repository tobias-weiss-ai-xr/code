/* bspl0012.c */
#include <stdio.h>

int main(void)
{
  int wahl;
  float betrag;
  printf("\n\t\tEUROUMRECHNER\n");
  printf("\n1 DM\t-->\t EURO\n");
  printf("\n2 EURO\t-->\t DM\n");
  printf("\nIhre Wahl: ");
  scanf("%i",&wahl);
  if ( wahl == 1 ) {
    printf("Bitte DM-Betrag eingeben: ");
    scanf("%f",&betrag);
    printf("\n%.2f DM sind %.2f EURO.\n",betrag,betrag*0.511);
  }
  if ( wahl == 2 ) {
    printf("Bitte EURO-Betrag eingeben: ");
    scanf("%f",&betrag);
    printf("\n%.2f EURO sind %.2f DM.\n",betrag,betrag/0.511);
  }
  return 0;
}
