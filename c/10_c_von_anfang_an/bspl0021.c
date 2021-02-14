/* bspl0021.c */
#include <stdio.h>

int main(void)
{
  int x,i;
  double zahl,sum;
  printf("\n\t\tS t a t i s t i k - Mittelwert\n");
  printf("Wieviele Werte wollen Sie eingeben?: ");
  scanf("%i",&x);
  for(i=1;i<=x;i++)
  {
    printf("Bitte den %i. Wert eingeben: ",i);
    scanf("%lf",&zahl);
    sum=sum+zahl;
  }
  printf("Die Summe der %i Zahlen betraegt %lf.\n",x,sum);
  printf("Der Mittelwert der %i Zahlen betraegt %lf.\n",x,sum/x);
  return 0;
}
