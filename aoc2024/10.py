from collections import defaultdict, deque

def count_paths_II(x, y, grid, curr):
	row, col = len(grid), len(grid[0])
	if x < 0 or x >= row or y < 0 or y >= col:
		return 0
	if grid[x][y] != str(curr): return 0
	if grid[x][y] == "9": # here is the only logical difference
		point = (x,y)
		return 1
	r = count_paths_II(x+1, y, grid, curr+1)
	l = count_paths_II(x-1, y, grid, curr+1)
	d = count_paths_II(x, y+1, grid, curr+1)
	u = count_paths_II(x, y-1, grid, curr+1)
	return r + l + d + u

def count_paths(x, y, grid, curr, visited):
	# start dfs from x, y until you hit 9

	# base case --> when we hit 9: return 1
	# when all the outgoing nodes are visited and no more path: return 0
	# there are 4 paths: call in 4 directions and sum all of them and return
	# this is bottom up
	# print('args', x,y,curr)
	row, col = len(grid), len(grid[0])
	if x < 0 or x >= row or y < 0 or y >= col:
		# print('out of bounds')
		return 0
	if grid[x][y] != str(curr): return 0
	if grid[x][y] == "9":
		point = (x,y)
		if point not in visited:
			visited.add((x,y))
			return 1
		return 0
	r = count_paths(x+1, y, grid, curr+1, visited)
	l = count_paths(x-1, y, grid, curr+1, visited)
	d = count_paths(x, y+1, grid, curr+1, visited)
	u = count_paths(x, y-1, grid, curr+1, visited)
	return r + l + d + u


def part1(grid):
	# find the start points
	start_points = []
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "0":
				start_points.append((i,j))

	# print(start_points)
	ans = 0
	for x, y in start_points:
		visited = set()
		a= count_paths(x, y, grid, 0, visited)
		# print(f"starting from {x} {y} the ans is {a}")
		ans += a
	return ans


def part2(grid):
	# why is the part 2 easier
	start_points = []
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "0":
				start_points.append((i,j))

	ans = 0
	for x, y in start_points:
		a = count_paths_II(x, y, grid, 0)
		ans += a
	return ans

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")
	grid = []
	for line in data:
		grid.append(list(line))

	print(part1(grid))
	print(part2(grid))




