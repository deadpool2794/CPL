 # List to store the records from dataset.txt
mid = -1  # Variable to store the middle index

def getData():
    """
    Read each line from dataset.txt and append it to records.
    """
    records = myList()  # Create a list to store the records 
    with open('dataset.txt', 'r') as f:
        for line in f:
            records.append(line.strip())
    return records  # Return the number of records read

def avg(a, b):
    """
    Calculate the average of two numbers and store it in mid.
    """
    global mid  # Use global keyword to modify the global variable
    mid = (a + b) // 2  # Calculate the middle index

def compareStrings(s1, s2, n):
    """
    Compare two strings character by character up to the given length.
    Return the difference in ASCII values of the first differing character,
    or 0 if the strings are equal.
    """
    for i in range(n):
        if s1[i] == ':' or s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])
    return 0
    
class myList(list): # Inherit from list class
    def binarySearch(self):
        """
        Perform binary search on the records list to find the key.
        Print the records that match the key.
        """
        # Your code here
        low, high = 0, len(self) - 1  # Initialize the low and high indices
        leftBoundary, rightBoundary = -1, -1  # Initialize the boundary variables

        key = input("Enter the key: ")  # Get the key from the user

        while low <= high:
            avg(low, high)  # Calculate the middle index
            # print("block variable address", hex(id(mid))) # Print the id of mid
            if compareStrings(self[mid], key, len(key)) < 0:
                low = mid + 1
            else:
                high = mid - 1
        if low == len(self) or not self[low].startswith(key):
            print("Key not found.")
            return
        leftBoundary = low
        high = len(self) - 1
        while low <= high:
            avg(low, high)  # Calculate the middle index
            if compareStrings(self[mid], key, len(key)) <= 0:
                low = mid + 1
            else:
                high = mid - 1
        rightBoundary = low - 1
        for i in range(leftBoundary, rightBoundary + 1):
            print(self[i])


if __name__ == '__main__':
    mid = -1  # Reset the value of mid
    # print("local variable address",hex(id(mid))) # Print the id of mid
    records = getData()  # Read data from dataset.txt
    records.binarySearch()  # Perform binary search
