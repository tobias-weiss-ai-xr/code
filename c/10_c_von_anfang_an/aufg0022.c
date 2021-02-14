/* aufg0022.c */
#include <stdio.h>

int main(void)
{
  int x;
  do {
  printf("\nBitte negative Zahl eingeben: ");
  scanf("%i",&x);
  } while(x>-1);
  printf("Die eingegebene Zahl lautet %i.\n",x);
}

