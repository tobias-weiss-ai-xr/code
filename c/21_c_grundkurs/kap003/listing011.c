 /* file: listing011.c
  * creator: TW
  * Last modified:  2014 Sep 12 19:40:01
  */

#include <stdio.h>
#include <math.h>

int main(void)
{
  double dval;
  printf("Fliesskommazahl eingeben: ");
  scanf("%lf", &dval);
  if( dval == HUGE_VAL ){
      printf("Achtung: ERANGE-Error\n");
      return 1;
  }
  printf("Die Zahl lautet: %lf\n", dval);
  return 0;
}

