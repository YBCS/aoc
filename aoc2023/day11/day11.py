# aoc day 11

data = open('test.txt', 'r').read().split('\n')

def part1(data):
	print(data)
	ROW = len(data)
	COL = len(data[0])
	expanded = ['' for _ in range(ROW)]
	print(expanded)
	# I forgot to expand the cols too
	for i in range(COL):
		col = ""
		for j in range(ROW):
			col += data[j][i]

		if col == "." * ROW:
			for k in range(ROW):
				expanded[k] += col[k]
				expanded[k] += col[k]
		else:
			for k in range(ROW):
				expanded[k] += col[k]

	# in the interest of time, I didn't want to break what I had build before; todo: refactor
	data = expanded
	expanded = []
	# [print(ex) for ex in expanded]

	id = 1
	pos = {} # store position of galaxy
	a = 0
	for i, galaxy in enumerate(data):
		if galaxy == "." * len(galaxy):
			expanded.append(galaxy)
			expanded.append(galaxy)
			a += 2
		else:
			new_g = ""
			for j, g in enumerate(galaxy):
				if g == "#":
					pos[id] = [a, j]
					new_g += str(id)
					id += 1
				else:
					new_g += g
			expanded.append(new_g)
			a += 1

	[print(ex) for ex in expanded]
	# I dont really need anything other than the pos dict
	print(f"pos is \n {pos}")
	
	ans = 0
	for i in range(1, len(pos)+1):
		for j in range(i+1, len(pos)+1):
			shortest_distance = abs(pos[j][0] - pos[i][0]) + abs(pos[j][1] - pos[i][1])
			ans += shortest_distance
			print(f'distance between {j} and {i} is {shortest_distance}') 
		print()
	print(ans) # 9795148


def part2(data):
	ROW = len(data)
	COL = len(data[0])
	expanded = ['' for _ in range(ROW)]
	EXPAND_BY = 100000 # this is insane 🤕
	for i in range(COL):
		col = ""
		for j in range(ROW):
			col += data[j][i]

		if col == "." * ROW:
			for k in range(ROW):
				for _ in range(EXPAND_BY):
					expanded[k] += col[k]
		else:
			for k in range(ROW):
				expanded[k] += col[k]

	data = expanded
	expanded = []

	id = 1
	pos = {} # store position of galaxy
	a = 0
	for i, galaxy in enumerate(data):
		if galaxy == "." * len(galaxy):
			for _ in range(EXPAND_BY):
				expanded.append(galaxy)
			a += EXPAND_BY
		else:
			new_g = ""
			for j, g in enumerate(galaxy):
				if g == "#":
					pos[id] = [a, j]
					new_g += str(id)
					id += 1
				else:
					new_g += g
			expanded.append(new_g)
			a += 1

	ans = 0
	for i in range(1, len(pos)+1):
		for j in range(i+1, len(pos)+1):
			shortest_distance = abs(pos[j][0] - pos[i][0]) + abs(pos[j][1] - pos[i][1])
			ans += shortest_distance
			print(f'distance between {j} and {i} is {shortest_distance}') 
		print()
	print(ans) # 9795148


part2(data)


