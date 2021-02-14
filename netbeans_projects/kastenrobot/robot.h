/* 
 * File:   robot.h
 * Author: homaar
 *
 * Created on August 26, 2014, 5:04 PM
 */

#ifndef ROBOT_H
#define	ROBOT_H

#ifdef	__cplusplus
extern "C" {
#endif

#include <stdbool.h>

    enum Action {
        left,
        right,
        up,
        down,
        put,
        fetch
    };

    typedef enum Action Action;

    struct Motion {
        Action a;
        unsigned int count;
    };

    typedef struct Motion Motion;

    void initialize(int h, int w);
    void finalize(void);
    bool execute(Action a, int count);
    void display(void);
    int getHeight(void);
    int getWidth(void);
    int getCount(int y, int x);
    int getInv(void);

#ifdef	__cplusplus
}
#endif

#endif	/* ROBOT_H */

