#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RECORD_LENGTH 100

#define MAX_LINES 1000000 // Maximum number of records in the file

char *records[MAX_LINES]; // Array to store records from the file
int mid; // Variable to store the middle index

// Function to read data from the file and store it in the records array
int getData(){
    FILE *file;
    int ind = 0;

    // Open the file
    file = fopen("dataset.txt", "r");
    if (file == NULL)
    {
        printf("Failed to open the file.\n");
        return 1;
    }

    // Read and store each line
    while (ind < MAX_LINES)
    {
        records[ind] = malloc(MAX_RECORD_LENGTH * sizeof(char));
        if (fgets(records[ind], MAX_RECORD_LENGTH, file) == NULL)
            break;
        ind++;
    }

    // Close the file
    fclose(file);
    return ind; // Return the number of records read
}

// Function to calculate the average of two numbers
void avg(int a, int b)
{
    // static scoping
    mid = (a + b) / 2; // Calculate the middle index
}

// Function to compare two strings up to a given length
int compareStrings(const char *s1, const char *s2, int n)
{
    for (int i = 0; i < n; i++)
    {
        if (s1[i] == ':' || s1[i] != s2[i])
            return s1[i] - s2[i]; // Compare characters and return the difference
    }
    return 0; // Strings are equal
}

// Function to perform binary search on the records array
void binarySearch(int len){
    int low = 0, high = len - 1;
    int leftBoundary = -1, rightBoundary = -1;

    char key[MAX_RECORD_LENGTH];
    printf("Enter the key: ");
    scanf(" %99[^\n]", key); // Read the key from the user

    while (low <= high)
    {
        avg(low, high); // Calculate the middle index
        // printf("%p\n", &mid); // print the address of mid
        if (compareStrings(records[mid], key, strlen(key)) < 0)
            low = mid + 1; // Update the lower bound
        else
            high = mid - 1; // Update the upper bound
    }

    if (low == len || compareStrings(records[low], key, strlen(key)) != 0)
    {
        printf("Key not found.\n");
        return;
    }

    leftBoundary = low; // Set the left boundary
    low = 0, high = len - 1;

    while (low <= high)
    {
        avg(low, high); // Calculate the middle index
        if (compareStrings(records[mid], key, strlen(key)) <= 0)
            low = mid + 1; // Update the lower bound
        else
            high = mid - 1; // Update the upper bound
    }

    rightBoundary = low - 1; // Set the right boundary

    // Print the records containing the key
    for (int i = leftBoundary; i <= rightBoundary; ++i)
        printf("%s", records[i]);
}

int main()
{
    int len = getData(); // Read data from the file
    int mid = -1; // Initialize the middle index
    // printf("local variable address : %p\n", &mid); // print the address of mid
    // Perform binary search
    binarySearch(len);

  

    // Free the allocated memory
    for (int i = 0; i < len; i++)
    {
        free(records[i]);
    }

    return 0;
}