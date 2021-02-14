 /* file: aufgabe001.c
  * creator: TW
  * Last modified:  2014 Sep 16 05:49:49
  */

#include <stdio.h>

int main(void)
{
  int ivalA = -1;
  unsigned int uvalB = 1;
  if ( ivalA > (int)uvalB ) { // Der unsigned int Typ muss explizit gecastet werden!
      printf("ivalA > uvalB");
  } else {
      printf("ivalA < uvalB");
  }
  
  return 0;
}

