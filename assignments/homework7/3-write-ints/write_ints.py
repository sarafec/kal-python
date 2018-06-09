import random, os

def write100Ints():
    filename = input("Please enter a filename: ")
    if not os.path.isfile(filename):
        startListCreation(filename)
    else:
        print("This file already exists.")

def startListCreation(filename):
    file = open(filename, "w")
    listOfNums = createStringOfNums()
    file.write(listOfNums)
    file.close()

def createStringOfNums():
    numbers = createListOfNums()
    return ' '.join(numbers)

def createListOfNums():
    listNums = []
    for i in range(0, 100):
        listNums.append(str(random.randint(0, 100)))
    
    return listNums

write100Ints()