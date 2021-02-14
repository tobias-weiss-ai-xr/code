/* aufg0018_a.c */
#include <stdio.h>

int main(void)
{
  int zeile,spalte;
  for(zeile=1; zeile <= 20; zeile++){
    for(spalte=20; spalte >= zeile; spalte--){
      printf("*"); 
    }
    printf("\n"); 
  }
  return 0;
}
