def letter_frequency(sentence):
	frequencies = {}
	for letter in sentence:
		# setdefault either puts the item in the dict with a default val and returns the entry
		# or it returns the current entry
		frequencies.setdefault(letter, 0)
		frequencies[letter] += 1

	return frequencies

d = letter_frequency("I love icecream")
for letter, frequency in d.items():
	print("{} occurs {} times(s).".format(letter, frequency))