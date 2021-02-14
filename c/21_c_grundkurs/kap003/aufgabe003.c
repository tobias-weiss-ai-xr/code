 /* file: aufgabe001.c
  * creator: TW
  * Last modified:  2014 Sep 10 16:03:47
  */

#include <stdio.h>

int main(void)
{
  double zahl;
  printf("Bitte eine Temperatur in ° Celsius eingeben: ");
  scanf("%lf", &zahl);
  printf("\nDie Temperatur betraegt in ° F: %lf\n", ((zahl*9/5)+32));
  printf("Die Temperatur betraegt in ° K: %lf\n", zahl+273.15);
  return 0;
}

