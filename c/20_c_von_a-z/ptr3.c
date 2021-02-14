/* ptr3.c */
#include <stdio.h>
#include <stdlib.h>

int main(void){
  int x=5;
  int *y;

  // printf("Adresse x=%p, Wert x=%d\n", &x,x);
  // printf("Adresse *y=%p, Wert *y=%d(unsinn)\n", &y, *y);
  
  printf("\ny=&x\n\n");
  y=& x; // Zeiger y auf x zeigen lassen

  printf("Adresse x=%p, Wert x=%d\n", &y, *y);
  printf("\nAdresse *y=%p, Wert *y=%d\n", &y, *y);
  printf("\nAdresse, auf die y zeigt, ist %p\n", y);
  printf("und das ist die Adresse von x =%p\n", &x);

  printf("ACHTUNG!!\n\n");
  *y=10;
  printf("y=10\n\n");
  printf("Adresse x=%p, Wert x=%d\n", &x, x);
  printf("Adresse *y=%p, Wert *y=%d\n", &y, *y);
  printf("weiterhin die Adresse vpn c (%p)\n", &x);
  return EXIT_SUCCESS;
}
