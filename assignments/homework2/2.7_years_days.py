import math

def displayYearsDays():
	minutes = eval(input("Enter number of minutes: "))
	MIN_IN_YEAR = 525600
	MIN_IN_DAY = 1440

	if (minutes < 0):
		return 'Invalid entry';

	# calculate years
	years = math.floor(minutes/MIN_IN_YEAR)
	minutes = minutes % MIN_IN_YEAR

	# calculate days
	days = minutes/MIN_IN_DAY;

	print(minutes, "minutes is", years, "years and", days, "days")

displayYearsDays()
