
# CPL

The provided codes are part of a binary search algorithm implemented in C and Python. Here's a step-by-step breakdown:

The main function begins by calling getData(), which presumably reads data from a file and returns the length of the data. This length is stored in len.

There are two variables named mid. One of these variables is likely used to store the middle index of the search space during the binary search. The other variable is declared to explain static scoping.

The binarySearch(len) function is invoked to execute a binary search on the data. This function performs two individual binary searches: one to find the first occurrence and another to find the last occurrence of a name containing a prefix that matches the key. It then prints all the records from the first to the last occurrence.



## Authors

- [@deadpool2794](https://github.com/deadpool2794)


## Requirements
Requires c/c++ compiler
C:
```
gcc -o bswithc .\BinarySearch.c
.\bswithc.exe
```
Python:
```
python BinarySearch.py

```
## Comparisions
### Garbage Collection:
Garbage collection plays a crucial role in managing memory in both C and Python. C,being a systems level programming language, memory management is primarily manual. The absence of built-in automatic garbage collection in C requires explicit memory allocation and deallocation using functions like malloc() and free(). In order to read each record from dataset malloc is used to explicitly declare memory in heap and free() is used to free the complete records array using for loop after iteration. This manual memory management can lead to memory leaks or dangling pointers if not handled carefully.

Conversely, Python, being a high-level language, employs an automatic garbage collector. Python's garbage collector automatically handles memory allocation and reclamation. It utilizes reference counting and a cyclic garbage collector to identify and collect unreferenced objects, freeing up memory automatically. This automatic memory management simplifies programming in Python by relieving developers from explicit memory deallocation concerns present in C, thereby reducing the likelihood of memory-related errors and making Python code more readable and maintainable.

### Scope
Both programming languages utilize static scoping for variable access within a block. To demonstrate this, I've added two 'mid' variables in the code. By uncommenting lines 69 and 105 in the C file, and lines 44 and 68 in the Python file, the memory addresses of the 'mid' variables used in the code are printed. 

This reveals that the 'mid' variable accessed in the binarySearch function comes from the global scope rather than the main block that calls binarySearch function. This distinction is clearly visible in the C code. However, in Python, the printed memory addresses alternate between two consecutive values within the binarySearch block. This behavior is due to Python's handling of immutable objects, like integers, where modifying them creates a new memory location. Nevertheless, the memory address of the 'mid' variable in the main block is entirely different from what is being printed within the binarySearch block.

### Parameter Passing

