 /* file: listing014.c
  * creator: TW
  * Last modified:  2014 Sep 12 20:41:31
  */

#include <stdio.h>

int main(void)
{
  int ival;
  double dval;
  printf("sizeof(ival): %lu\n", sizeof(ival));
  printf("sizeof(dval): %lu\n", sizeof(dval));
  // so gehts auch
  printf("sizeof(float): %lu\n", sizeof(float));

  return 0;
}

