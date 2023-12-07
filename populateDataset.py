import names_dataset
import random
import regex as re

def generateRandomNumber():
    """
    Generate a random 10-digit number.

    Returns:
        str: Random 10-digit number.
    """
    return ''.join([str(random.randint(0, 9)) for i in range(10)])

def matches_regex(string):
    """
    Check if a string matches a regular expression pattern.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    return bool(re.fullmatch(regex, string))


nd = names_dataset.NameDataset()
uniqueNumbers = set()
allRecords = []
regex = r'[a-zA-Z ]*'

# Iterate over the top names dataset
for country, info in nd.get_top_names(n=100000).items():
    for gender, names in info.items():
        for name in names:
            number = generateRandomNumber()
            # Check if the name matches the regex pattern and the generated number is unique
            if(matches_regex(name) and (number not in uniqueNumbers)):
                allRecords.append(name + ":" + number)
                uniqueNumbers.add(number)

allRecords.sort()

# Open file dataSet.txt in write mode and write allRecords to it
with open('dataset.txt', 'w') as f:
    for record in allRecords:
        f.write(record + "\n")












