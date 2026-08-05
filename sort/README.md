# CCSORT

Implementation of the Unix Command Line Tool sort

## Running
```bash
gcc sort.c heapsort.c mergesort.c quicksort.c radixsort.c randomsort.c -o sort
./sort [OPTIONS] [FILEPATH]
```

## Functionality
```bash
sort [OPTION]... [INPUT]
Sorts the lines from INPUT (or standard input).
OPTIONS:
With no FILE, or when FILE is -, read standard input
-m, --merge-sort Merge Sort
-q, --quick-sort Quick Sort
-R, --random-sort Random Sort
-r, --radix-sort Radix Sort
-u, print unique elements
```