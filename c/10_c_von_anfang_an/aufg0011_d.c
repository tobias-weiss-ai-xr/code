/* aufg0011_d.c */
#include <stdio.h>

int main(void){
  int n1=1,n2=17;
  if(n1 > 0 && n2 > 0 || n1 > n2 && n2 != 17){
    printf("\nTRUE\n");
  } else 
    printf("\nFALSE\n");
  return 0;
}
