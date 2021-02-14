/* aufg0007.c */
#include <stdio.h>

int main(void)
{
  float verbrauch,km;
  printf("\n\t\t Benzinverbrauchsrechner\n");
  printf("Bitte geben Sie den Benzinverbrauch/100 Km an: ");
  scanf("%f",&verbrauch);
  printf("\nBitte geben Sie die gefahrenen Kilometer an: ");
  scanf("%f",&km);
  printf("\nDer gesamte Benzinverbrauch betraegt ");
  printf("%.2f Liter.\n",km / verbrauch);
  return 0;
}
