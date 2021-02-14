/* bspl0018.c */
#include <stdio.h>

int main(void){
  int jahr,monat,tage;
  printf("\nK A L E N D E R");
  printf("\nBitte Jahr eingeben: ");
  scanf("%i",&jahr);
  printf("\nBitte Monat eingeben: ");
  scanf("%i",&monat);
  if (monat >=1 && monat <=12 && jahr > 1852){
    switch (monat){
    case 2:
      if (!(jahr%100)%4 && (jahr%100) || !(jahr%400))
        tage = 29;
      else
        tage = 28;
      break;
    case 2*2:
    case 6:
    case 9: case 11:
      tage = 30;
      break;
    default:
      tage = 31;
    }
  printf("\n%i hat der Monat %i %i Tage.\n",jahr,monat,tage);
  } else
  printf("Falsche Datumsangabe.\n");
  return 0;
}
