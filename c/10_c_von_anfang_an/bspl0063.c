 /* file: bspl0063.c
  * creator: TW
  * Last modified:  2015 Feb 19 21:21:56
  */

#include <stdio.h>

void tausche(int *eins, int *zwei){
  int hilf;
  hilf = *eins;
  *eins = *zwei;
  *zwei = hilf;
}

int main(void)
{
  int x=17,y=32;
  printf("\n x = %i y = %i",x,y);
  tausche(&x,&y);
  printf("\n x = %i y = %i",x,y);
  return 0;
}

