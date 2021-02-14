 /* file: aufgabe002.c
  * creator: TW
  * Last modified:  2014 Sep 16 05:53:32
  */

#include <stdio.h>

int main(void)
{
  char cval;
  int ival;
  float fval=1234.123;
  double dval;
 
  cval = fval;
  ival = fval;
  dval = fval;

  printf("cval : %c\n", cval);
  printf("ival : %d\n", ival);
  printf("dval : %lf\n", dval);
  return 0;
}

