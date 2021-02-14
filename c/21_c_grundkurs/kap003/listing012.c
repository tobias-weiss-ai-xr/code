 /* file: listing012.c
  * creator: TW
  * Last modified:  2014 Sep 12 19:45:27
  */

#include <stdio.h>

int main(void)
{
  int ival=1;
  printf("ival: %d\n", ival);
  ival++;
  printf("ival: %d\n", ival);
  printf("ival: %d\n", ival++);
  printf("ival: %d\n", ival);
  printf("ival: %d\n", ++ival);

  return 0;
}

