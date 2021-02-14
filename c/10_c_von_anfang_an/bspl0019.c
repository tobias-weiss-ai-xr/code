/* bspl0019.c */
#include <stdio.h>
#include <ctype.h>

int change(void){
  char eingabe;
  int zahl;
  printf("\nWaehlen Sie (O)ktal,(H)exadezimal oder (A)SCII > ");
  scanf(" %c",&eingabe);
  printf("\nBitte Dezimalzahl eingeben: ");
  scanf("%i",&zahl);
  switch(toupper(eingabe)){
    case 'O':
		printf("Dezimal %i = Oktal %o \n",zahl,zahl);
		break;
    case 'H':
		printf("Dezimal %i = Hexadezimal %x \n",zahl,zahl);
		break;
    case 'A':
		if(zahl<=255)
			printf("Dezimal %i = ASCII %c \n",zahl,zahl);
		else
			printf("Diese Zahl ist zu gross!\n\a");
		break;
    default:
		printf("\nKeine gueltige Eingabe!\n");
  }
  return 0;
}

int main(void)
{
  int killer=0;
  char temp;
  while(killer==0){
  change();
  printf("\nNochmal? (Y/N): ");
  scanf(" %c",&temp);
  if(toupper(temp)=='Y')
   killer=0;
  else
    killer=1;
  }
  return 0;
}
