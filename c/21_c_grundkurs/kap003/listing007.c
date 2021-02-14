 /* file: listing007.c
  * creator: TW
  * Last modified:  2014 Sep 12 10:39:12
  */

#include <stdio.h>

int main(void)
{
  int val1, val2, val3;
  int sum, mul, rest;

  printf("Rechnen mit 3 Ganzzahlen\n");
  printf("------------------------\n");
  printf("Wert 1: ");
  scanf("%d", &val1);
  printf("Wert 2: ");
  scanf("%d", &val2);
  printf("Wert 3: ");
  scanf("%d", &val3);

  sum = val1 + val2 + val3;
  printf("%d + %d + %d = %d\n", val1, val2, val3, sum);
  mul = val1 * val2 * val3;
  printf("%d * %d * %d = %d\n", val1, val2, val3, mul);
  rest = (val1 * val2) % val3;
  printf("(%d * %d) / %d = %d Rest: %d\n", val1, val2, val3, (val1*val2)/val3, rest);

  return 0;
}

