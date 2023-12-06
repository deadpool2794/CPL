import names_dataset
import random
import regex as re

def generateRandomNumber():
    return ''.join([str(random.randint(0, 9)) for i in range(10)])

def matches_regex(string):
    return bool(re.fullmatch(regex, string))


nd = names_dataset.NameDataset()
uniqueNumbers = set()
allRecords = []
regex = r'[a-zA-Z ]*'

for country, info in nd.get_top_names(n=100000).items():
    for gender, names in info.items():
        for name in names:
            number = generateRandomNumber()
            if(matches_regex(name) and (number not in uniqueNumbers)):
                allRecords.append(name + ":" + number)
                uniqueNumbers.add(number)

allRecords.sort()


# open file dataSet.txt in write mode and write allRecords to it
with open('dataset.txt', 'w') as f:
    for record in allRecords:
        f.write(record + "\n")












