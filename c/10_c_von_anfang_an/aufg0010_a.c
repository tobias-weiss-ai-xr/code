/* aufg0010_a.c */
#include <stdio.h>

int main(void)
{
  float x;
  printf("\n\t\tKehrwert\n");
  printf("Bitte Zahl eingeben: ");
  scanf("%f",&x);
  printf("\nDer Kehrwert der Zahl lautet ");
  printf("%f\n",(x > 0) ? -x : x);
  return 0;
}
