CC=g++
CFLAGS=-c
WFLAGS= -g 

all: mat.o  evaluate

mat.o:main.cpp mat.h
	$(CC) $(WFLAGS) $(CFLAGS) $< -o $@

evaluate: mat.o
	$(CC) $(WFLAGS) $^ -o $@    


clean:
	rm -rf *.o
	rm -rf evaluate
