# CCWC

Implementation of the Unix Command Line Tool wc


## Running
```bash
cd wc
./build.sh # for Linux 
./build.ps1 # for Windows
./ccwc [OPTIONS] [FILEPATH]
```

## Functionality
```bash
ccwc [OPTIONS].. [FILE]..
Print newline, word, and byte counts for each FILE
OPTIONS:
With no FILE, or when FILE is -, read standard input
-c Number of bytes in a file
-m Number of lines in a file
-w Number of words in a file
-m Number of characters in a file
```