/* aufg0006.c */
#include <stdio.h>

int main(void)
{
  float schlaege,alter;
  printf("\n\t\tHerzschlaege\n");
  printf("\nHerzschlaege pro Minute:\t");
  scanf("%f",&schlaege);
  printf("Alter in Jahren:\t");
  scanf("%f",&alter);
  printf("\nIhr Herz hat seit Ihrer Geburt ");
  printf("%f ", schlaege * 60 * 24 * 365.25 * alter);
  printf("mal geschlagen\n");
  return 0;
}
