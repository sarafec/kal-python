def convertCelsiustoFahrenheit():
	tempInCelsius = eval(input("Enter degrees in celsius: "))
	
	fahrenheit = (9/5) * tempInCelsius + 32
	print("Degrees in Fahrenheit: ", fahrenheit)

convertCelsiustoFahrenheit()