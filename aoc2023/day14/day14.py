# aoc day 14
data = open('input.txt', 'r').read().split('\n')

def moveONorth(col):
	out = ""
	l = 0
	r = 0
	while r < len(col):
		o_count, d_count = 0, 0
		while r < len(col) and col[r] != '#':
			if col[r] == "O":
				o_count += 1
			else: # dot count
				d_count += 1
			r += 1

		zeroes = 'O'*o_count
		dots = '.'*d_count
		out += zeroes+dots
		out += "#" if r<len(col) else ""
		l = r
		r += 1
	# print('out is ', out)
	return out

def part1(data):
	'''
	move the 0 far north as possible
	count 0 in each row and multiply by row no.
	
	# lets work in transpose because I cannot deal with this 🤕
	'''
	# print(data)
	[print(d) for d in data]
	print()
	ans = 0
	north = []
	for i in range(len(data[0])):
		
		col = ""
		for j in range(len(data)):
			col += data[j][i]
		# print('col is ', col)
		col = moveONorth(col)
		north.append(col)
		
	[print(n) for n in north]
	c = 0
	for i in range(len(north[0])):
		o_count = 0
		for j in range(len(north)):
			if north[j][i] == "O":
				o_count += 1
		c += o_count * (len(north[0]) - i)
		print('final c is ', c, o_count)

	return ans



# part1(data)
col = "OO.O.O..##" # 'OOOO....##'
col = ".O...#O..O" # 'O....#OO..'
col = ".O...####O..O..OOO#.#" # 'O....#OO..'
col = "OO.O.O..##OO#O" # 'OOOO....##'
moveONorth(col)
