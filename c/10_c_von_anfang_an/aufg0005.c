/* aufg0005.c */
#include <stdio.h>

int main(void){
  float celsius;
  printf("\nBitte Grad Celsius eingeben:");
  scanf("%f",&celsius);
  printf("\n%.1f Grad Celsius entsprechen ",celsius);
  printf("%.1f Grad Fahrenheit. \a",celsius*9/5+32);
  return 0;
}
