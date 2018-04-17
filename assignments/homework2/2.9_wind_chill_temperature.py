def calculateWindChill():
	temp = eval(input("Enter the current temperature: "))
	windspeed = eval(input("Enter the current windspeed: "))
	windchill = 35.74+ (0.6215 * temp) - (35.75 * (windspeed ** 0.16)) + (0.4275 * temp * (windspeed ** 0.16))

	print("With the current windchild, the temperature is:", windchill)

calculateWindChill()