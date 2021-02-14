/* bspl0040.c */
#include <stdio.h>
#include <string.h>

int main(void)
{
  char geheim[10],passwort[80];
  int versuch=3;
  geheim[3]='p';
  geheim[2]=109;
  geheim[7]=114;
  geheim[5]=116;
  geheim[0]=67;
  geheim[9]='x';
  geheim[1]=111;
  geheim[8]='\0';
  geheim[4]=geheim[1]+6;
  geheim[6]=101;
  printf("Sie haben %i Versuche.\n",versuch);
  do 
  {
  printf("\nBitte Passwort eingeben: \n");
  gets(passwort);
  if(strcmp(geheim,passwort) == 0){
    printf("\nPasswort ok!\n");
    break;
  } else
    printf("\nFalsches Passwort! \n");
    versuch--;
  }
  while(versuch>0);
  return 0;
}

