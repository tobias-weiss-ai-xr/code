 /* file: aufgabe001.c
  * creator: TW
  * Last modified:  2014 Sep 16 05:29:25
  */

#include <stdio.h>

int main(void)
{
  int var1, var2;
  printf("Zahl1 eingeben: ");
  scanf("%d", &var1);
  printf("Zahl2 eingeben: ");
  scanf("%d", &var2);
  printf("%d + %d = %d", var1, var2, var1+var2);

  return 0;
}

