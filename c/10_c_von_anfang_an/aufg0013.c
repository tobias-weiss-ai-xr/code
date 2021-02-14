/* aufg0013.c */
#include <stdio.h>

int main (void) {
  float temp;
  printf("\n\t\tWasserverhalten\n");
  printf("Bitte Temperatur eingeben: ");
  scanf("%f",&temp);
  if(temp<4){
    printf("\nBei einer Temperatur von %.2f gefriert das Wasser!\n",temp);
  } else if (temp<100)
    printf("\nBei einer Temperatur von %.2f passiert gar nichts!\n",temp);
  else
    printf("\nBei einer Temperatur von %.2f kocht das Wasser!\n",temp);
  return 0;
}
