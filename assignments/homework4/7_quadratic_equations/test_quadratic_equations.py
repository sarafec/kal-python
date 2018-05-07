from quadraticEquations import QuadraticEquation

def runQuadraticEquation():
	a = float(input("Please enter your 'a' value: "))
	b = float(input("Please enter your 'b' value: "))
	c = float(input("Please enter your 'c' value: "))
	userDefinedQE = QuadraticEquation(a,b,c)
	discriminant = userDefinedQE.getDiscriminant()

	if discriminant > 0:
		print("Root One: ", userDefinedQE.getRoot1())
		print("Root Two: ", userDefinedQE.getRoot2())
	elif discriminant == 0:
		print("Root One: ", userDefinedQE.getRoot1())
	else:
		print("The equation has no roots")

runQuadraticEquation()