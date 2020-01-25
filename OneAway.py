def OneAway(str_1, str_2):

	if len(str_1) == len(str_2):
		print(len(str_1), len(str_2))
		return replace(str_1, str_2)
	elif len(str_1) + 1 == len(str_2):
		return insert(str_1, str_2)
	elif len(str_1) - 1 == len(str_2):
		return insert(str_1, str_2)

def replace(s1, s2):
	difference = False
	i = 0
	while i < len(s1):
		if s1[i] != s2[i]:
			if difference:
				return False
		else:
			difference = True
			return True
		i+=1
			

def insert(s1, s2):
	index_1 = 0
	index_2 = 1

	while index_2 < len(s2) and index_1 < len(s1):
		if s1[index_1] != s2[index_2]:
			if index_1 != index_2:
				return False
				index_2+=1

			else:
				index_1+=1
				index_2+=2
		return True

print(OneAway('pale','pale'))