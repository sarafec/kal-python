# write a program to display the FUN pattern
pattern = [["FFFFFFF   U     U   NN     NN"], ["FF        U     U   NNN    NN"], ["FFFFFFF   U     U   NN N   NN"], ["FF         U   U    NN  N  NN"], ["FF          UUU     NN    NNN"]]

for i in range(len(pattern)):
	print(''.join(pattern[i]))
