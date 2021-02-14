/* bspl0016.c */
#include <stdio.h>

int main(void)
{
  int x = 5, y = 11, z = 3;
  int ergebnis, resultat;
  ergebnis = x < y;
  resultat = x || z < y;
  if (ergebnis)
    printf("\nx ist kleiner als y!\n");
  else
    printf("\nx ist groesser als y!\n");
  printf("\n%i\n",resultat);
  return 0;
}
