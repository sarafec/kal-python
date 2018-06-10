from tkinter import *

canvas_width = 300
canvas_height = 300


def drawGraph():
    filename = input("Please input file name: ")
    numOfNodes, linesInFile = openFile(filename)
    coords = createCoordList(linesInFile)
    neighbors = createEdgesList(linesInFile)

    window = Tk()
    window.title("Graph")
    canvas = Canvas(window, width=canvas_width, height=canvas_height)
    drawNodes(linesInFile, canvas)
    drawEdges(coords, neighbors, canvas)
    canvas.pack()
    window.mainloop()


def createCoordList(data):
    dictionary = {}
    for line in range(0, len(data)):
        for item in range(0, len(data[line])):
            if item == 0:
                dictionary[data[line][0]] = []
            elif item == 1:
                dictionary[data[line][0]].append(data[line][item])
            elif item == 2:
                dictionary[data[line][0]].append(data[line][item])
    return dictionary

def createEdgesList(data):
    dictionary = {}
    for line in range(0, len(data)):
        for item in range(0, len(data[line])):
            if item == 0:
                dictionary[data[line][0]] = []
            elif item > 2:
                dictionary[data[line][0]].append(data[line][item])
    return dictionary

def drawNodes(data, canvas):
    for line in range(0, len(data)):
        canvas.create_oval(data[line][1], data[line][2], data[line][1], data[line][2])

def drawEdges(coords, neighbors, canvas):
    for key, value in neighbors.items():
        for item in range(0, len(value)):
            x1, y1 = coords[key]
            x2, y2 = coords[value[item]]
            canvas.create_line(x1, y1, x2, y2)


def openFile(filename):
    file = open(filename, 'r')
    numOfNodes = file.readline()
    linesInFile = []
    for line in file:
        convertedLine = [int(x) for x in line.split(" ")]
        linesInFile.append(convertedLine)
    return numOfNodes, linesInFile

drawGraph()
