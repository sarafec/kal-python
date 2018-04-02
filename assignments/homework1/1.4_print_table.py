# write a program that displays the following table

tableVals = [1, 2, 3, 4]

print("a    a^2    a^3")

for i in range(len(tableVals)):
	print '%-6i%-6i%-6i' % (tableVals[i], (tableVals[i] ** 2), (tableVals[i] ** 3))
