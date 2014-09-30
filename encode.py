def encode(str):
	global codes
	output =''
	for ch in str : output +=codes[ch]
	return output
print encode('aabccdeeeeeffg')
