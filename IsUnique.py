def IsUnique(string):
	d = {}

	for letter in range(len(string.lower())):
		if string[letter] not in d:
			d[string[letter]] = letter
	if len(string) > len(d):
		return print("{} is NOT a [UNQIUE] string".format(string))
	else:
		return print("{} is a [UNIQUE] String!".format(string))