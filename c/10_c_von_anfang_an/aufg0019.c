/* aufg0019.c */
#include <stdio.h>

int main(void)
{
  int i,n,prod=1;
  printf("\n\tn-te Fakultaet --> n!");
  printf("\nBitte geben Sie n ein: ");
  scanf("%i",&n);
  for(i=1;i<=n;i++){
    prod = prod*i;  
  }
  printf("Die Fakultaet betraegt %i.\n",prod);
  return 0;
}
