/* bspl0023.c */
#include <stdio.h>
#include <ctype.h>

int main(void)
{
  double zahl;
  printf("\n\tQ U A D R A T Z A H L E N\n");
  printf("\nBitte Dezimalzahl eingeben :");
  scanf("%lf",&zahl);
  while(zahl!=0){
    printf("\nDas Quadrat der Zahl %.2lf betraegt %.4lf.\nBitte neue Zahl eingeben (0 beendet das Programm): \n",zahl,zahl*zahl);
    scanf("%lf",&zahl);
  }
  return 0;
}
