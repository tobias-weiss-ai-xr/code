 /* file: bspl0061.c
  * creator: TW
  * Last modified:  2015 Feb 19 21:17:36
  */

#include <stdio.h>

int main(void)
{
  int zahl;
  int *ptr;
  zahl = 88;
  ptr = &zahl;
  printf("\nDer Wert von 'zahl' ist %i", zahl);
  printf("\nDie Adresse von 'zahl' ist %u", ptr);
  printf("\nDie Groesse von 'ptr ist %u", sizeof(ptr));
  printf("\n'ptr' zeigt auf den Wert %i", *ptr);
  return 0;
}

