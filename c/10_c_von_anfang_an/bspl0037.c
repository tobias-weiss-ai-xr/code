/* bspl0037.c */
#include <stdio.h>
#include <string.h>

int main(void)
{
  char satz[80];
  size_t laenge;
  printf("\nBitte einen Satz eingeben: \n");
  gets(satz);
  printf("\n%s",satz);
  laenge = strlen(satz);
  printf("\nDer Satz besteht aus %d Zeichen.\n",laenge);
  printf("\n\nsatz[5] enthaelt eine binaere Null.\n");
  satz[5]='\0';
  printf("\n%s",satz);
  laenge = strlen(satz);
  printf("\nDer Satz besteht aus %d Zeichen.\n",laenge);
  return 0;
}
