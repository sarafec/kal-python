def calculateEnergy():
	waterInKg = eval(input("Enter amount of water in kilograms: "))
	initialTemp = eval(input("Enter initial temperature: "))
	finalTemp = eval(input("Enter final temperature: "))
	
	energy = waterInKg * (finalTemp - initialTemp) * 4184
	
	print(energy, "joules")

calculateEnergy()