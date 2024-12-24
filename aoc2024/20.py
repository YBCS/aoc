from collections import defaultdict, deque, Counter
from functools import cache
import heapq
import math
import sys
import re

dirs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

# cp template.py day_no.py
# https://topaz.github.io/paste/
# time <python_file.py>
# python3 -m <python_file>
# python3 -m <python_file> <inp.txt>

def pr(data):
	print("data ", data)

def print_grid(grid):
	# for line in grid:
	# 	print("".join(list(map(str, line))))
	[print(row) for row in grid]
	# [print("".join(row)) for row in grid]

# does not work....
def part1(data):
	grid = []
	row = len(data)
	col = len(data[0])

	for i in range(row):
		grid.append(list(data[i]))
		for j in range(col):
			if data[i][j] == "S":
				sr, sc = i, j 		# row, col
			if data[i][j] == "E":
				er, ec = i, j 		# row, col

	grid = [[-1] * col for _ in range(col)]
	r, c = sr, sc
	grid[r][c] = 0
	while data[r][c] != "E":
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if not (0 <= nr < row) or not (0 <= nc < col): # out of bounds
				continue
			if data[nr][nc] == "#": # going into walls
				continue 
			if grid[nr][nc] != -1: # visited
				continue
			grid[nr][nc] = grid[r][c] + 1
			r = nr
			c = nc

	# print_grid(grid)
	_dirs = [(2,0), (2,2), (0,2), (-2,2)]
	ans = 0
	for i in range(row):
		for j in range(col):
			if data[i][j] == "#":
				continue
			for dr, dc in _dirs:
				nr, nc = i + dr, j + dc
				if not (0 <= nr < row) or not (0 <= nc < col): continue
				# if nr < 0 or nc < 0 or nr >= row or nc >= col: continue
				if data[nc][nc] == "#": continue
				# print("saved time ", abs(grid[i][j] - grid[nr][nc]))
				if abs(grid[i][j] - grid[nr][nc]) >= 102:
					ans += 1
	print("ans is ", ans)


# def part1(data):
# 	grid = []
# 	row = len(data)
# 	col = len(data[0])

# 	for i in range(row):
# 		grid.append(list(data[i]))
# 		for j in range(col):
# 			if data[i][j] == "S":
# 				sr, sc = i, j 		# row, col
# 			if data[i][j] == "E":
# 				er, ec = i, j 		# row, col

# 	grid = [["#"] * col for _ in range(col)]
# 	r, c = sr, sc
# 	grid[r][c] = 0
# 	while data[r][c] != "E":
# 		for dr, dc in dirs:
# 			nr, nc = r + dr, c + dc
# 			if not (0 <= nr < row) or not (0 <= nc < col): # out of bounds
# 				continue
# 			if data[nr][nc] == "#": # going into walls
# 				continue 
# 			if grid[nr][nc] != "#": # visited
# 				continue
# 			grid[nr][nc] = grid[r][c] + 1
# 			r = nr
# 			c = nc
# 	print_grid(grid)	

def part2():
	pass

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")
	# 6781 ## too high
	part1(data)
	# part2()




