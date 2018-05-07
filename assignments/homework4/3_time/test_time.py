from time import Time


def askElapsedTime():
	time = Time()
	print("Current time is " + str(time.getHour()) + ":" + str(time.getMinute()) + ":" + str(time.getSecond()))
	elapsedTime = float(input("Enter the elapsed time: "))
	print("The elapsed time is ", time.setTime(elapsedTime))

askElapsedTime()
