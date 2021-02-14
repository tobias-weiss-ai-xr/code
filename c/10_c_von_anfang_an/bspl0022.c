/* bspl0022.c */
#include <stdio.h>

int main(void)
{
  int x,y,dim;
  printf("\n\t\tZahlengitter\n");
  printf("Wieviele Werte wollen Sie eingeben?: ");
  scanf("%i",&dim);
  for(x=1;x<=dim;x++)
  {
    for(y=1;y<=dim;y++)
    {
      printf("%4i",x*y);  
    }
    printf("\n");
  }
  return 0;
}
