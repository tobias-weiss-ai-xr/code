/* aufg0014.c */
#include <stdio.h>
#include <ctype.h>

int main(void){
  float temperatur;
  char zeichen;
  printf("\n\tT E M P E R A T U R R E C H N E R\n");
  printf("\n1 Fahrenheit \n2 Raumur\n3 Kelvin\n4 Rankine\n0 Ende \
  \n\nAuswahl: ");
  zeichen = getchar();
  switch (zeichen){
    case '0':
      break;
    case '1': case '2': case '3': case '4':
      printf("\nBitte Grad Celsius eingeben: ");
      scanf("%f",&temperatur);
      if(temperatur >= -273.15){
	  switch(zeichen){
	  case '1':
	    printf("\n%.2f °C sind %.2f °F.\n",temperatur,9/5*temperatur+32);
	    break;
	  case '2':
	    printf("\n%.2f °C sind %.2f °R.\n",temperatur,4/5*temperatur);
            break;
	  case '3':
	    printf("\n%.2f °C sind %.2f K.\n",temperatur,temperatur+273.15);
            break;
	  case '4':
	    printf("\n%.2f °C sind %.2f °Rank.\n",temperatur,9/5*(temperatur+273.15));
            break;  
	}
      } else
    printf("Diese Temperatur gibt es nicht!\n");
    break;
  default:
    printf("\nUngueltige Option!\n");
  }
  return 0;
}
