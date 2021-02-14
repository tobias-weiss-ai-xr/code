/* aufg0032.c */
#include <stdio.h>
#include <string.h>

int main(void)
{
  int i;
  char puffer[20];
  strcpy(puffer,"Programmiersprache C   asdf");
  for(i;i<20;i++)
  {
    printf("%c\n",puffer[i]);
    printf("%d\n",puffer[i]);
  }
  return 0;
}


