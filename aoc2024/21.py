from collections import defaultdict, deque, Counter
from functools import cache
import heapq
import math
import sys
import re

up = (-1,0,"^")
right = (0,1,">")
down = (1,0,"v")
left = (0,-1,"<")
dirs = [(-1,0,"^"),(0,1,">"),(1,0,"v"),(0,-1,"<")] # up right down left
dirs = [up, left, down, right] # up right down left

# cp template.py day_no.py
# https://topaz.github.io/paste/
# time <python_file.py>
# python3 -m <python_file>
# python3 -m <python_file> <inp.txt>

def pr(data):
	print("data ", data)

def print_grid(grid):
	# [print(row) for row in grid]
	[print("".join(row)) for row in grid]

numpad_grid = [	["7", "8", "9"], 
				["4", "5", "6"], 
				["1", "2", "3"], 
				["None", "0", "A"]]

dirpad_grid = [	["None", "^", "A"],
				["<", "v", ">"]]


# not just one ; but all of them
def find(grid, target, sr, sc):
	# print('in find ', sc, grid[sr][sc])
	row = len(grid)
	col = len(grid[0])
	# queue = deque([(sr,sc, "")])
	queue = []
	heapq.heappush(queue, (0,sr,sc,"")) # dist, sr, sc, path
	visited = set()
	visited.add((sr, sc))
	while queue:
		# r, c, path = queue.popleft()
		dist, r, c, path = heapq.heappop(queue)

		if grid[r][c] == target:
			return (r,c,path+"A", dist)

		for dr, dc, char in dirs:
			nr, nc = r + dr, c + dc
			if not ( 0 <= nr < row ) or not ( 0 <= nc < col ):
				continue
			if (nr, nc) in visited:
				continue
			if grid[nr][nc] == "None":
				continue
			# print("visiting ", nr, nc, grid[nr][nc])
			visited.add((nr,nc))
			heapq.heappush(queue, (dist+1, nr, nc, path+char))
			# queue.append((nr, nc, path+char))
		# print("the heapq ", queue)

	print("should not get out of grid ")

def part1(data):
	# out = find(numpad_grid, "5", 3, 2)
	# out = find(dirpad_grid, "<", 0, 2)
	# print('out ', out)


	for line in data:
		path = ""
		r, c = 3, 2
		for char in line:
			r,c, _path, dist = find(numpad_grid, char, r, c)
			# print("outputs", r,c, _path)
			path += _path

		print("path for robot 1 ", path, dist, len(path))

		# r, c = 0, 2
		# path_2 = ""
		# for char in path:
		# 	r, c, _path, dist = find(dirpad_grid, char, r, c)
		# 	path_2 += _path
		# 	# print("outputs", r,c, _path)
		# print("path for robot 2 ", path_2, dist, len(path_2))


		# r, c = 0, 2
		# path_3 = ""
		# for char in path_2:
		# 	r, c, _path, dist = find(dirpad_grid, char, r, c)
		# 	path_3 += _path
		# # print()
		# print("path for robot 3 ", path_3, dist, len(path_3))
	pass
def part2():
	pass

if __name__ == "__main__":	
	file = "in.txt"
	file = "eg.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")

	part1(data)
	part2()




