/* aufg0012.c */
#include <stdio.h>

int main(void){
  char bstb;
  printf("\nBitte geben Sie ein beliebiges Zeichen ein: ");
  bstb=getchar();
  if(bstb < 'A' || bstb > 'z' || (bstb > 'Z' && bstb < 'a') ){
    printf("\n %c ist kein Buchstabe!\n",bstb);
  } else if (bstb >= 'A' && bstb <= 'Z') {
    printf("\n %c ist ein Grossbuchstabe!",bstb);
  } else
    printf("\n %c ist ein Kleinbuchstabe!",bstb); 
return 0;
}
