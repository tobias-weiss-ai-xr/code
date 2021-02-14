/* aufg0010.c */
#include <stdio.h>

int main(void)
{
  float x,y;
  printf("\n\t\tZahlenvergleich\n");
  printf("Bitte erste Zahl eingeben: ");
  scanf("%f",&x);
  printf("\nBitte zweite Zahl eingeben: ");
  scanf("%f",&y);
  printf("\nDie groessere Zahl lautet ");
  printf("%f\n",(x > y) ? x : y);
  return 0;
}
