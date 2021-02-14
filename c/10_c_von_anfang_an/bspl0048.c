/* bspl0048.c */
#include <stdio.h>
#include "bspl0048.h"

int main(void){
    double x=4711.0,y=11.0;
    printf("Ergebnis = %f\n", func(x,y));
    return 0;
}

double func(double x, double y){
    return (x/y);
}
