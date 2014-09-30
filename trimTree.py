def trimTree(tree):
	p=tree[1]
	if type(p) == type(""): return p
	else: return (trimTree(p[0]), trimTree(p[1]))
print trimTree([(1, 'b'), (1, 'd'), (1, 'g'), (2, 'c'), (2, 'f'), (3, 'a'), (5, 'e')] )
