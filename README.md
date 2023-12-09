# CPL

The languages I've selected are C(procedural programming paradigm) and Python (multi-paradigm) . 

Given that C is a purely functional language, I've implemented functions for performing binary search and comparing strings. In the Python code, I've utilized a custom myList class that inherits from the built-in Python list class. This custom `myList` class includes an additional method, binarySearch, encapsulated as a method within the myList class objects

The provided codes are part of a binary search algorithm implemented in C and Python. Here's a step-by-step breakdown:

The main function begins by calling `getData()`, which presumably reads data from a file and returns the length of the data in C.This length is stored in a variable and used later in different parts of code. Whereas in python, the function returns a reference to the records object, facilitating access to its built-in method `len()` to determine the length of the retrieved data.

There are two variables named mid. One of these variables is likely used to store the middle index of the search space during the binary search. The other variable is declared to explain static scoping.

The `binarySearch(len)` function is invoked to execute a binary search on the data in C.Since binarySearch is defined as a class method, it can be accessed using the dot `.` operator without the necessity of passing any arguments explicitly. This function/method performs two individual binary searches: one to find the first occurrence and another to find the last occurrence of a name containing a prefix that matches the key. It then prints all the records from the first to the last occurrence.


Note: Comparision is case sensitive. populateDataset.py is used to create "dataset.txt" file. Executing this program would create dataset.txt file in the current directory containing 970K "Name:PhoneNumber" records which can be used to test binarySearch functions in both the files.


## Authors

- [@deadpool2794](https://github.com/deadpool2794)


## Requirements
Requires c/c++ compiler and python interpreter

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
Garbage collection plays a crucial role in managing memory in both C and Python. C,being a systems level programming language, memory management is primarily manual. The absence of built-in automatic garbage collection in C requires explicit memory allocation and deallocation using functions like `malloc()` and `free()`. In order to read each record from dataset `malloc()` is used to explicitly declare memory in heap and `free()` is used to free the complete records array using for loop after iteration. This manual memory management can lead to memory leaks or dangling pointers if not handled carefully.

Conversely, Python, being a high-level language, employs an automatic garbage collector. Python's garbage collector automatically handles memory allocation and reclamation. It utilizes reference counting and a cyclic garbage collector to identify and collect unreferenced objects, freeing up memory automatically. This automatic memory management simplifies programming in Python by relieving developers from explicit memory deallocation concerns present in C. This reduces the likelihood of memory-related errors and making Python code more readable and maintainable.

### Scope
Both programming languages utilize static scoping for variable access within a block. To demonstrate this, I've added two 'mid' variables in the code. By uncommenting lines 69 and 105 in the C file, and lines 44 and 68 in the Python file, the memory addresses of the 'mid' variables used in the code are printed. 

This reveals that the 'mid' variable accessed in the binarySearch function comes from the global scope rather than the main block that calls binarySearch function. This distinction is clearly visible in the C code. However, in Python, the printed memory addresses alternate between two or more but repeated values within the binarySearch block. This behavior is due to Python's handling of immutable objects, like integers, where modifying them creates a new memory location. Nevertheless, the memory address of the 'mid' variable in the main block is entirely different from what is being printed within the binarySearch block.

### Parameter Passing

In both C and Python files, I've utilized the `compareString` function to demonstrate parameter passing. This function takes three arguments: the first two are strings, and the third is an integer representing the length up to which both strings are compared.

In C, strings are commonly represented as arrays of characters terminated by a null character `\0`. When passing a string to a function, it involves passing a pointer to the first character of the string, and this pointer is passed by value. Consequently, while the pointer itself is passed by value, the content of the string it points to can be modified within the function. Moreover, the length parameter passed to compareString in C is also passed by value. Changing its value within the compareString function does not alter anything in the binarySearch function. This is because alterations to the value of the length parameter within the compareStrings function remain confined within its local scope and do not affect values in the binarySearch function.

In Python, integers, along with other immutable objects like strings, tuples, etc., are passed by object reference. When an integer or any other immutable object is passed to a function, a reference to that object is passed. However, due to the immutability of integers, direct modification of the original integer within the function is not possible. If an attempt is made to modify it within a function block, such as in the compareString function, a new object of that integer type (or other immutable object like a string) is implicitly created in the local scope of that function. Consequently, the value of the newly created object will be changed within the function, but the original values in the binarySearch function remain unchanged.