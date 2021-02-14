/* bspl0008.c */
#include <stdio.h>

int main(void){
  float summe=0.0,zahl;
  printf("\n1. Zahl: ");
  scanf("%f",&zahl);
  summe=summe+zahl;
  printf("2. Zahl: ");
  scanf("%f",&zahl);
  summe=summe+zahl;
  printf("3. Zahl: ");
  scanf("%f",&zahl);
  summe=summe+zahl;
  printf("\nEndergebnis: %.17f\n",summe);
  return 0;
}
