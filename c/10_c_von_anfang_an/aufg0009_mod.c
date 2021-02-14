/* aufg0009.c */
#include <stdio.h>

int main(void)
{
  double summe=0.0,zahl;
  printf("\nBitte geben Sie eine Zahl ein: ");
  scanf("%lf",&zahl);
  summe = summe + zahl;
  summe = summe + zahl;
  printf("Ergebnis = %lf\n",summe);
  return 0;
}
