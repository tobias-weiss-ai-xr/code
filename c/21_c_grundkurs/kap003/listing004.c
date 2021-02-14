 /* file: listing004.c
  * creator: TW
  * Last modified:  2014 Sep 12 09:49:50
  */

#include <stdio.h>
#include <float.h>

int main(void)
{
  printf("float Genauigkeit: %d\n", FLT_DIG);
  printf("double Genauigkeit: %d\n", DBL_DIG);
  printf("long double Genauigkeit: %d\n", LDBL_DIG);
  return 0;
}

