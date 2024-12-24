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
	[print("".join(row)) for row in grid]

def part1():
	pass
def part2():
	pass

if __name__ == "__main__":	
	file = "in.txt"
	file = "eg.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")

	part1()
	part2()




