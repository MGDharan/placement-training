def drawPattern(n):
	for x in range(0, n):
		for y in range(0, n):
			if x>=y:
				print(' * ', end='')
		print('')
		
drawPattern(6)
