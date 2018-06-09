def promptUser():
    filename = input("Please enter filename: ")
    text = open(filename, 'r').read()
    countCharacters(text)
    countWords(text)
    countLines(filename)

def countCharacters(text):
    numOfChars = len(text)
    print(numOfChars)

def countWords(text):
    numOfwords = text.split()
    print(len(numOfwords))

def countLines(filename):
    with open(filename) as f:
        print(len(list(f)))

promptUser()