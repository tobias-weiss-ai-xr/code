/* bspl0005.c */

#include <stdio.h>

int main(void) {
    int x,y;
    printf("\n\t1 . R e c h e n p r o g r a m m\n");
    printf("Bitte x eingeben :");
    scanf("%i", &x);
    printf("Bitte y eingeben :");
    scanf("%i", &y);
    printf("\n %i + %i ist %i",x,y,x+y);
    printf("\n %i - %i ist %i",x,y,x-y);
    printf("\n %i * %i ist %i",x,y,x*y);
    printf("\n %i %% %i ist %i\n\n",x,y,x%y);
    return 0; 
}

