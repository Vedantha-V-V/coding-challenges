# CCCAT

Implementation of the Unix Command Line Tool cat

## Running
```bash
gcc -o cccat cccat.c
./cccat [OPTIONS] [FILEPATH]
```

## Functionality
```bash
cccat [OPTIONS].. [FILE]..
Prints contents of File(s) to standard output
OPTIONS:
With no FILE, or when FILE is -, read standard input
-n Number the lines as they are printed out
-b Number the non empty lines as they are printed out
```