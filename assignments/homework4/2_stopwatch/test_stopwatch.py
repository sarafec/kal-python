from stopwatch import StopWatch
import time


def howLongToCountNumbers(startNum, endNum):
	stopwatch = StopWatch(time.time())
	stopwatch.start()
	sum = 0
	for i in range(startNum, endNum):
		sum += i
	stopwatch.stop()
	print(stopwatch.getElapsedTime())

howLongToCountNumbers(1, 1000000)