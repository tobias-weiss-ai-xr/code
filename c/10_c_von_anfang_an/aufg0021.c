/* aufg0021.c */
#include <stdio.h>

int main(void)
{
  int i=1,sum,x;
  printf("\n\t Gerade Zahlen");
  printf("\nBitte geben Sie die groesste Zahl an: ");
  scanf("%i",&x);
  while(i<=x){
    if(i%2==0){
    printf("%i\n",i);
    sum=sum+i;
    }
    i++;
  }
  printf("\nDie Summe der Zahlen betraegt %i.\n",sum);
  return 0;
}
