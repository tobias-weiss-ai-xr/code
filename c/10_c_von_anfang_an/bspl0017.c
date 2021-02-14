/* bspl0017.c */
#include <stdio.h>

int main(void)
{
  int a,b,erg;
  printf("\nW A H R H E I T S T A B E L L E N\nImplikation\n");
  a=0,b=0,erg=!(a&&!b);
  printf("\n%i\t%i\t%i\n",a,b,erg);
  a=0,b=1,erg=!(a&&!b);
  printf("\n%i\t%i\t%i\n",a,b,erg);
  a=1,b=0,erg=!(a&&!b);
  printf("\n%i\t%i\t%i\n",a,b,erg);
  a=1,b=1,erg=!(a&&!b);
  printf("\n%i\t%i\t%i\n",a,b,erg);
  return 0;
}
