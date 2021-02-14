CC=g++
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS = -std=c++17 -g -Wall

default: snake

tetris:
	$(CC) $(CFLAGS) tetris.cpp -o tetris

snake:
	$(CC) $(CFLAGS) snake.cpp -o snake -lncurses

sales: 
	$(CC) $(CFLAGS) sales.cpp -o sales

clean:
	$(RM) sales tetris
