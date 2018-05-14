from collections import defaultdict

def letter_frequency(sentence):
	frequencies = defaultdict(int)
	for letter in sentence:
		frequencies[letter] += 1

	return frequencies

d = letter_frequency("I love icecream")
for letter, frequency in d.items():
	print("{} occurs {} times(s).".format(letter, frequency))