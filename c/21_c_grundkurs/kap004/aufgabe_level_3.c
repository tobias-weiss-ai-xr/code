 /* file: aufgabe_level_3.c
  * creator: TW
  * Last modified:  2014 Okt 05 19:47:34
  */

#include <stdio.h>

int main(void)
{
  int z1;
  float fz1;
  double lfz1,delta;

  printf("Bitte eine Zahl eingeben: ");
  scanf("%lf", &lfz1);

  z1=lfz1;
  fz1=z1;
  delta=lfz1-z1;

  printf("z1: %i\nfz1: %f\nlfz1: %f\ndelta: %f\n", z1, fz1, lfz1, delta);

  return 0;
}

