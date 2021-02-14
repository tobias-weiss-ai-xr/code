/* bspl0013.c */
#include <stdio.h>

int main(void){
  float temp;
  printf("\n\t\tTemperaturumrechner\n");
  printf("\nBitte Temperatur in ° Celsius eingeben: ");
  scanf("%f",&temp);
  if ( temp >= -273.15){
    printf("Die Temperatur %.2f ° Celsius betraegt %.2f ° Kelvin.\n",temp,temp+273.15);
  } else {
    printf("\nDiese Temperatur gibt es leider nicht!\n");
  }
  return 0;
}
