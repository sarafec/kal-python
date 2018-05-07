from fan import Fan

fan1 = Fan(3, 10, "yellow")
fan1.setFanState(True)
print("Fan One")
print("-- Speed:", fan1.getFanSpeed())
print("-- Radius:", fan1.getFanRadius())
print("-- Color:", fan1.getFanColor())
print("-- Is it on?", fan1.getFanState())
print("\n")

fan2 = Fan(2, 5, "blue")
fan2.setFanState(False)
print("Fan Two")
print("-- Speed:", fan2.getFanSpeed())
print("-- Radius:", fan2.getFanRadius())
print("-- Color:", fan2.getFanColor())
print("-- Is it on?", fan2.getFanState())