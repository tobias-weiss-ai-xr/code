/*
 * File:   newsimpletest.c
 * Author: homaar
 *
 * Created on Aug 26, 2014, 7:01:14 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include "robot.h"

/*
 * Simple C Test Suite
 */

void testInizialize() {
    inizialize();
    if (1 /*check result*/) {
        printf("%%TEST_FAILED%% time=0 testname=testInizialize (newsimpletest) message=error message sample\n");
    }
}

int main(int argc, char** argv) {
    printf("%%SUITE_STARTING%% newsimpletest\n");
    printf("%%SUITE_STARTED%%\n");

    printf("%%TEST_STARTED%%  testInizialize (newsimpletest)\n");
    testInizialize();
    printf("%%TEST_FINISHED%% time=0 testInizialize (newsimpletest)\n");

    printf("%%SUITE_FINISHED%% time=0\n");

    return (EXIT_SUCCESS);
}
