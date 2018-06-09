def promptUser():
	filename = input("Please enter filename: ")
	text = input("Please enter text to be removed: ")
	removeText(text, filename)


def removeText(text, filename):
	infile = open(filename, "r")
	fullText = infile.read()
	modifiedFullText = fullText.replace(text, '')
	infile.close()

	outfile = open(filename, 'w')
	outfile.write(modifiedFullText)
	outfile.close()

	printConfirmation()

def printConfirmation():
	print("Done!")

promptUser()

# todo: is there a way to do this without opening the file twice?