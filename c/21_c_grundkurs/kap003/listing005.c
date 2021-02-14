 /* file: listing005.c
  * creator: TW
  * Last modified:  2014 Sep 12 09:56:06
  */

#include <stdio.h>

int main(void)
{
  float wkursF = 1.4906;
  float betragF = 100100.12;

  double wkursD = 1.4906;
  double betragD = 100100.12;

  printf("[float]  : %f Dollar = %f Euro\n", betragF, betragF/wkursF);
  printf("[double] : %lf Dollar = %lf Euro\n", betragD, betragD/wkursD);
  return 0;
}

