/* 
 * File:   robot.c
 * Author: homaar
 *
 * Created on August 26, 2014, 5:04 PM
 */
#include "robot.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Spielfeld
static unsigned char *field;
static int height, width;

//Startwerte des Roboters
static int x = 0; //width
static int y = 0; //height
static int inv = 0;

void initialize(int h, int w) {
    height = h;
    width = w;
    field = (unsigned char*) malloc(h * w);
    int i;
    for (i = 0; i < height; i++) {
        int j;
        for (j = 0; j < width; j++) {
            field[4 * i + j] = rand() % 5 + 1;
        }
    }
}

void finalize(void) {
    free(field);
}

bool execute(Action a, int count) {
    Motion m = {a, count};
    bool ret = true;
    int i;
    for (i = 0; i < m.count; i++) {
        switch (m.a) {
            case up:
                if (y == 0) {
                    ret = false;
                } else {
                    y--;
                }
                break;
            case down:
                if (y >= height - 1) {
                    ret = false;
                } else {
                    y++;
                }
                break;
            case left:
                if (x == 0) {
                    ret = false;
                } else {
                    x--;
                }
                break;
            case right:
                if (x >= width - 1) {
                    ret = false;
                } else {
                    x++;
                }
                break;
            case fetch:
                if (field[4 * y + x] == 0) {
                    ret = false;
                } else {
                    inv++;
                    field[4 * y + x]--;
                }
                break;
            case put:
                if (inv == 0) {
                    ret = false;
                } else {
                    inv--;
                    field[4 * y + x]++;
                }
                break;
            default:
                ret = false;
        }
    }
    return ret;
}

int getHeight(void) {
    return height;
}

int getWidth(void) {
    return width;
}

int getCount(int y, int x) {
    return field[4 * y + x];
}

int getInv(void) {
    return inv;
}

void display(void) {
    int i; //height
    int j; //width
    for (i = -1; i < height; i++) {
        for (j = -1; j < width; j++) {
            if (i == -1) {
                if (j == x) {
                    putchar('V');
                } else {
                    putchar(' ');
                }
            } else if (j == -1) {
                if (i == y) {
                    putchar('>');
                } else {
                    putchar(' ');
                }
            } else
                putchar('0' + field[4 * i + j]);
        }
        putchar('\n');
    }
    printf("\nInventory: %i\n", inv);
    
}
