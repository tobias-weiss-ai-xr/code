 /* file: listing008.c
  * creator: TW
  * Last modified:  2014 Sep 12 10:43:11
  */

#include <stdio.h>

int main(void)
{
  double r, pi=3.14159265358979;
  double aKreis;

  printf("Kreisberechnung:\n");
  printf("----------------\n");
  printf("Radius angeben: ");
  scanf("%lf", &r);
  aKreis = r * r * pi;
  printf("Kreisflaeche bei Radius %.2lf betraegt %.2lf\n", r, aKreis);

  return 0;
}

