 /* file: listing014.c
  * creator: TW
  * Last modified:  2014 Sep 16 05:25:30
  */

#include <stdio.h>
#include <stddef.h> //fuer wchar_t Dateityp

int main(void)
{
  wchar_t ch1=L'Z';
  wchar_t ch2;
  printf("Bitte ein Zeichen eingeben: ");
  scanf("%lc", &ch2);
  printf("%lc %lc\n", ch1,ch2);
  printf("wchar_t %lu Bytes\n", sizeof(wchar_t)); // Long unsigned int Dateityp -->  %lu

  return 0;
}

