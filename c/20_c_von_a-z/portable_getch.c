 /* file: portable_getch.c
  * creator: TW
  * Last modified:  2015 Mär 13 22:26:42
  */

#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <unistd.h>

static struct termios new_io;
static struct termios old_io;

/* Switch terminal into cbreak mode
 * Set controlflag ECHO and ICANON to 0
 * Controlchar: Readoperation returns a byte VMIN=1 VTIME=1
 */

int cbreak(int fd) {
    /* Save terminal content*/
    if((tcgetattr(fd, &old_io)) == -1)
	return -1;
    new_io = old_io;
    /* Enlage flags for cbreak mode */
    new_io.c_lflag = new_io.c_lflag & ~(ECHO|ICANON);
    new_io.c_cc[VMIN] = 1;
    new_io.c_cc[VTIME] = 0;

    /* Change to cbreak mode */
    if((tcsetattr(fd, TCSAFLUSH, &new_io)) == -1)
	return -1;
    return 1;
}

int getch(void) {
    int c;

    if(cbreak(STDIN_FILENO) == -1) {
	printf("Error in cbreak function...\n");
	exit(EXIT_FAILURE);
    }
    c = getchar();
    /* restore previous terminal state */
    tcsetattr(STDIN_FILENO, TCSANOW, &old_io);
    return c;
}


int main(void) {
    int input;

    printf(" Enter 'q' to exit!\n");

    /* Wait for char 'q'*/
    while(( input =getch() ) != 'q');

    return EXIT_SUCCESS;
}
