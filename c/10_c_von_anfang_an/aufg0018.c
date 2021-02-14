/* aufg0018.c */
#include <stdio.h>

int main(void)
{
  int zeile,spalte;
  for(zeile=1; zeile <= 20; zeile++){
    for(spalte=1; spalte <= zeile; spalte++){
      printf("*"); 
    }
    printf("\n"); 
  }
  return 0;
}
