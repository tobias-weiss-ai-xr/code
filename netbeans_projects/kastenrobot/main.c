/* 
 * File:   main.c
 * Author: homaar
 *
 * Created on August 26, 2014, 5:04 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "robot.h"

/*
 * 
 */
int main(int argc, char** argv) {
    bool ret = true;
    int a,b;
    printf("Bitte Höhe eingeben:");
    scanf("%i",&a);
    printf("Bitte Breite eingeben:");
    scanf("%i",&b);
    printf("\n");
    initialize(5,5);
    int h = getHeight() - 1;
    int w = getWidth() - 1;
    int i = 0;
    int j = 0;
    for (i = 0; i <= h; i++) {
        if (i % 2 == 0) {
            for (j; j < w; j++) {
                ret &= execute(fetch, getCount(i, j));
                ret &= execute(right, 1);
            }
        } else {
            for (j; j > 0; j--) {
                ret &= execute(fetch, getCount(i, j));
                ret &= execute(left, 1);
            }
        }
        ret &= execute(fetch, getCount(i, j));
        if (i != h) {
            ret &= execute(down, 1);
        } else {
            ret &= execute(put, getInv());
        }
    }
    display();
    finalize();
    if (ret == true) {
        return (EXIT_SUCCESS);
    } else
        return (EXIT_FAILURE);
}

