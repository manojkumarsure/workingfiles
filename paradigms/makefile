CC=g++
CFLAGS=-c
WFLAGS= -g 

all: mat.o  a.out

mat.o:main.cpp mat.h
	$(CC) $(WFLAGS) $(CFLAGS) $< -o $@

a.out: mat.o
	$(CC) $(WFLAGS) $^ -o $@    


clean:
	rm -rf *.o
	rm -rf a.out
