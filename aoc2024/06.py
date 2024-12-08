

def part1(grid, start):
	path = set()
	i, j = start
	path.add((i,j))
	d_i, d_j = -1, 0
	n = len(grid[0]) - 1
	while not (i == 0 or j == 0 or i == n or j == n): # is not touching an edge
		i += d_i
		j += d_j
		if grid[i][j] == "#": # turn 90 degree
			i -= d_i
			j -= d_j
			# update d_i, d_j
			if d_i == -1 and d_j == 0: # up
				d_i, d_j = 0, 1
			elif d_i == 0 and d_j == 1: # right
				d_i, d_j = 1, 0
			elif d_i == 1 and d_j == 0: # down
				d_i, d_j = 0, -1
			elif d_i == 0 and d_j == -1: # left
				d_i, d_j = -1, 0
			continue
		path.add((i,j))

	print(len(path))


def part2(grid, start):
	n = len(grid[0]) - 1
	ans = 0
	# detect a cycle each time...
	# so place an obstacle everywhere and run the loop and check
	# if a path is crossed twice; there is a loop
	for a in range(len(grid)):
		for b in range(len(grid[0])):
			i, j = start
			d_i, d_j = -1, 0
			path = set()
			path.add((i, j, d_i, d_j))
			if grid[a][b] == "#":
				continue
			
			grid[a][b] = "#"
			while not (i == 0 or j == 0 or i == n or j == n): # is not touching an edge
				
				i += d_i
				j += d_j
				check =  (i, j, d_i, d_j)
				if check in path: # cycle
					ans += 1
					break

				if grid[i][j] == "#": # turn 90 degree
					i -= d_i
					j -= d_j
					# update d_i, d_j
					if d_i == -1 and d_j == 0: # up
						d_i, d_j = 0, 1
					elif d_i == 0 and d_j == 1: # right
						d_i, d_j = 1, 0
					elif d_i == 1 and d_j == 0: # down
						d_i, d_j = 0, -1
					elif d_i == 0 and d_j == -1: # left
						d_i, d_j = -1, 0
					continue

				path.add((i, j, d_i, d_j))

			grid[a][b] = "."

	print("ans is ", ans)

'''
00 01 02
10 11 12
20 21 22
'''

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")

	grid = []
	i = 0
	for line in data:
		grid.append(list(line))
		for j in range(len(line)):
			if line[j] == "^":
				start = (i,j)
		i += 1
	
	part1(grid, start)
	part2(grid, start)

