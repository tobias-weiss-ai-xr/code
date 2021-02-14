/* aufg0011_b.c */
#include <stdio.h>

int main(void){
  int zahl=10,wert=100; 
  if(zahl != 0 || zahl > wert || wert-zahl == 90){
    printf("\nTRUE\n");
  } else 
    printf("\nFALSE\n");
  return 0;
}
