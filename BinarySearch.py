MAX_LINES =  1000000

def getData():
    ind = 0
    lines = []

    # Open the file
    try:
        file = open("dataset.txt", "r")
    except IOError:
        print("Failed to open the file.")
        return 1

    # Read and store each line
    for line in file:
        if ind >= MAX_LINES:
            break
        lines.append(line.strip())
        ind += 1

    # Close the file
    file.close()
    return ind, lines  # Return the number of lines read and the lines themselves


def binarySearch(len, lines):
    low = 0
    high = len - 1
    leftBoundary = -1
    rightBoundary = -1

    key = input("Enter the key: ")

    while low <= high:
        mid = (low + high) // 2
        if lines[mid][:len(key)] < key:
            low = mid + 1
        else:
            high = mid - 1

    if low == len or lines[low][:len(key)] != key:
        print("Key not found.")
        return

    leftBoundary = low
    low = 0
    high = len - 1

    while low <= high:
        mid = (low + high) // 2
        if lines[mid][:len(key)] <= key:
            low = mid + 1
        else:
            high = mid - 1

    rightBoundary = low - 1

    for i in range(leftBoundary, rightBoundary + 1):
        print(lines[i])