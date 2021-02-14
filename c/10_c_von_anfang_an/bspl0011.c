/* bspl0011.c */
#include <stdio.h>

int main(void)
{
  int x,y,z;
  printf("\n\t\tZahlenvergleich\n");
  printf("Bitte die erste Zahl eingeben: ");
  scanf("%i",&x);
  printf("\nBitte die zweite Zahl eingeben: ");
  scanf("%i",&y);
  printf("\nBitte die dritte Zahl eingeben: ");
  scanf("%i",&z);
  printf("\nDie groesste Zahl lautet %i.\n",(x>y) ? ((x>z) ? x : z) : ((y>z) ? y : z));
  return 0;
}
