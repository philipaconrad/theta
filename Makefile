SHELL = /bin/sh
.SUFFIXES:
.SUFFIXES: .h .c .o .lib .s
THETA_SOURCES = theta.c

all: install

install:
	$(CC) -I. -I$(srcdir) $(CFLAGS) -g $(THETA_SOURCES) -g -lgmp -o theta.exe

clean:
	rm theta.exe
