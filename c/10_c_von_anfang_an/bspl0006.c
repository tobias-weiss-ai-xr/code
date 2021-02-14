/* bspl0006.c */

#include <stdio.h>

int main(void) {
    float x,y;
    printf("\n\t1 . R e c h e n p r o g r a m m\n");
    printf("Bitte x eingeben :");
    scanf("%f", &x);
    printf("Bitte y eingeben :");
    scanf("%f", &y);
    printf("\n %f + %f ist %f",x,y,x+y);
    printf("\n %f - %f ist %f",x,y,x-y);
    printf("\n %f * %f ist %f",x,y,x*y);
    printf("\n %f / %f ist %f\n\n",x,y,x/y);
    return 0; 
}

