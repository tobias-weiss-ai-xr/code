/* aufg0027.c */
#include <stdio.h>

double d_abs(double);
void beep(int);

int main(void){
  double x,abs;
  printf("\nAbsolutwerte\nBitte Zahl eingeben: ");
  scanf("%lf",&x);
  abs=d_abs(x);
  printf("Der Absolutwert von %.2lf betraegt %.2lf\n",x,abs);
  printf("Fuer jeden Wert ein Beep :-)\n");
  beep(abs);
  return 0;
}

double d_abs(double x){
  if(x<0){
    x*=-1;
  }
  return x;
}

void beep(int x){
  int i=0;
  while(i<x){
    printf("Alarmsound!!\a\n");
    i++;
  }
}
