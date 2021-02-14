/* aufg0029.c */
#include <stdio.h>

int vorzeichen(double);

int main(void){
  double x;
  printf("\n\tVorzeichencheck\n");
  printf("Bitte eine Zahl eingeben: ");
  scanf("%lf",&x);
  printf("Der Check ergab: %i.\n",vorzeichen(x)); 
  return 0;
}

int vorzeichen(double x){
  int ret=0; 
  if(x>0){
    ret=1;
  } else if (x<0) {
    ret=-1;
  }
  return ret;
}
