/* aufg0024.c */
#include <stdio.h>

double min(double x, double y){
  if(x<y){
    return x;
  } else
    return y;
}

int main(void)
{
  double x,y;
  printf("\n\tKleinere Zahl ausgeben\n");
  printf("Bitte erste Zahl eingeben: ");
  scanf("%lf",&x);
  printf("Bitte zweite Zahl eingeben: ");
  scanf("%lf",&y);
  printf("\nDie kleinere Zahl lautet %.2lf.\n",min(x,y));
  return 0;
}



