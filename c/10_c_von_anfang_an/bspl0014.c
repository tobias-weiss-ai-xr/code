/* bspl0014.c - Dieses Programm arbeitet nicht korrekt! */
#include <stdio.h>

int main(void){
  int x;
  printf("\nBitte Zahl eingeben: ");
  scanf("%i",&x);
  if(x<0) {
    printf("Die Zahl %i ist positiv.\n",x);
  } else {
    printf("Die Zahl %i ist negativ.\n",x);
  }
  return 0;
}
