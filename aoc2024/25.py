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
	# [print(row) for row in grid]
	print()
	[print("".join(row)) for row in grid]
	print()

def is_match(lock, key):
	for a,b in zip(lock, key):
		if a + b > 5:
			return False

	return True

def part1(data):
	locks = []
	keys = []
	for i in range(0, len(data), 8):
		grid = []
		for j in range(i, i+7):
			grid.append(list(data[j]))

		# print_grid(grid)

		if data[i] == "#####":
			# lock
			lock = []
			for j in range(5): # moving in row (left to right)
				k = 1
				height = 0
				while grid[k][j] == "#": # moving in col (up to down)
					height += 1
					k += 1
				lock.append(height)
			locks.append(lock)

		elif data[i] == ".....":
			# key
			key = []
			for j in range(5):
				k = 5
				height = 0
				while grid[k][j] == "#":
					height += 1
					k -= 1
				key.append(height)
			keys.append(key)

	# print("locks \t",locks)
	# print("keys \t",keys)
	
	ans = 0
	for lock in locks:
		for key in keys:
			if is_match(lock, key):
				ans += 1

	print(ans)


if __name__ == "__main__":	
	file = "in.txt"
	file = "eg.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")

	part1(data)
	# MERRY CHRISTMAS 🎅🏼🎄



