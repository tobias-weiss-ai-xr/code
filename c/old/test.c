#include <stdio.h>

void main(void)
{
  int c;
  printf("Test\n");
  c = getchar();
  while (c != EOF) {
    putchar(c);
    c = getchar();
  }
}
