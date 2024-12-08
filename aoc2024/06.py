file = "eg.txt"
file = "in.txt"
data = open(file, "r").read().split("\n")




grid = []
i = 0
for line in data:
	grid.append(line)
	for j in range(len(line)):
		if line[j] == "^":
			start = (i,j)
	i += 1

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


## part 2 is asking what ??

'''
00 01 02
10 11 12
20 21 22
'''

