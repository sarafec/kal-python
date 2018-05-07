from fan import Fan


def printFanStats(fan, state):
	fan.setFanState(state)
	print("Fan Stats")
	print("-- Speed:", fan.getFanSpeed())
	print("-- Radius:", fan.getFanRadius())
	print("-- Color:", fan.getFanColor())
	print("-- Is it on?", fan.getFanState())

fan1 = Fan(3, 10, "yellow")
fan2 = Fan(2, 5, "blue")
printFanStats(fan1, True)
print("\n")
printFanStats(fan2, False)