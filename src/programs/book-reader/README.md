# Book reader

**A simple book reader**

## Build

Adjust the variables in `build_book.py` and run `make book` to build the book from a text file to a series of PETSCII files.

The files are already included in the repository so this step is not necessary if you are running the program with the provided book.

If you want to build the book from a text file, run _from this directory_:

```bash
c64 $ make TARGET=programs/book-reader/book-reader book
```

## Run

From the _root directory_ of the repository, run:

```bash
c64 $ make TARGET=programs/book-reader/book-reader
```

## BASIC version

An XC=BASIC version of the book reader is available [here](/src/programs/xc-basic/book-reader).
