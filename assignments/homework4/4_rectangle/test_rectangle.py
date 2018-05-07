from rectangle import Rectangle


def printRectangleSpecs(rect):
	print("Rectangle One:")
	print("Area - " + str(rect.getArea()))
	print("Perimeter - " + str(rect.getPerimeter()))
	print("Width - " + str(rect.width)) 
	print("Height - " + str(rect.height))

rectangle1 = Rectangle(40, 4)
rectangle2 = Rectangle(35.7, 3.5)
printRectangleSpecs(rectangle1)
print("\n")
printRectangleSpecs(rectangle2)