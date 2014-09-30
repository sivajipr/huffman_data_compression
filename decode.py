def decode(tree, str):
	output =''
	for ch in str: output += codes[ch]
	return output
print decode((('a', ('g', 'c')), (('f', ('b', 'd')), 'e')) , 'aaabccdeeeeeffg')
