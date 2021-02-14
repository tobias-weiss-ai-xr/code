/* bspl0009.c */
#include <stdio.h>

int main(void){
  double summe=0.0,zahl;
  printf("\n1. Zahl: ");
  scanf("%lf",&zahl);
  summe=summe+zahl;
  printf("2. Zahl: ");
  scanf("%lf",&zahl);
  summe=summe+zahl;
  printf("3. Zahl: ");
  scanf("%lf",&zahl);
  summe=summe+zahl;
  printf("\nEndergebnis: %.17f\n",summe);
  return 0;
}
