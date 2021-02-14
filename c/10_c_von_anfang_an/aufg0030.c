/* aufg0030.c */
#include <stdio.h>

double hoch(double,int);

int main(void){
  double zahl;
  int potenz;
  printf("\n\tHochzahlen\n");
  printf("Bitte eine Zahl eingeben: ");
  scanf("%lf",&zahl);
  printf("Bitte die Potenz eingeben: ");
  scanf("%d",&potenz);
  printf("Die %i. Potenz oder Zahl %lf ist %lf.\n",potenz,zahl,hoch(zahl,potenz)); 
  return 0;
}

double hoch(double wert, int potenz){
  int i;
  double ret=wert;
  if(wert==0){
    ret=1;
  } else if(wert<0) {
    ret=-1;
  } else {
    for(i=1;i<potenz;i++){
      ret*=wert;
    }
  }
  return ret;
}
