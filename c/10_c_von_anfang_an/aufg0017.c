/* aufg0017.c */
#include <stdio.h>

int main(void)
{
  int i,x;
  printf("\n\t Gerade Zahlen");
  printf("\nBitte geben Sie die groesste Zahl an: ");
  scanf("%i",&x);
  for(i=1;i<=x;i++){
    if(i%2==0){
    printf("%i\n",i);
    }
  }
  return 0;
}
