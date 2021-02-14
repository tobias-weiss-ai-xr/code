/* aufg0010_b.c */
#include <stdio.h>

int main(void)
{
  float celsius;
  printf("\n\t\tCelsius\n");
  printf("Bitte Temperatur in Celsius eingeben: ");
  scanf("%f",&celsius);
  printf("\nDie Temperatur in Celsius betraegt ");
  printf("%f\n",(celsius < -273.15) ? -273.15 : celsius);
  return 0;
}
