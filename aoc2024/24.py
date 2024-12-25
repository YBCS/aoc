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

def part1(data):
	print(data)
	isBreak = False
	wires = {}
	instructions = {}

	for line in data:
		if not line:
			isBreak = True
			continue

		if not isBreak:

			wire, nu = line.split(" ")
			wire = wire[:-1]
			wires[wire] = int(nu)

			continue
		wire1, op, wire2, wire3 = line.replace(" -> ", " ").split(" ")
		instructions[wire3] = (wire1, op, wire2)

		# process the rest of the iput



	def solve(key):
		# if key already in instructions : return
		if key in wires: return wires[key] 
		wire1, op, wire2 = instructions[key]

		o1, o2 = None, None
		if wire1 in wires:
			o1 = wires[wire1]
		if wire2 in wires:
			o2 = wires[wire2]
		
		if not o1:
			o1 = solve(wire1)
		if not o2:
			o2 = solve(wire2)

		if op == "XOR":
			ans =  o1 ^ o2
		elif op == "OR":
			ans = o1 | o2
		elif op == "AND":
			ans = o1 & o2

		wires[key] = ans
		return ans

	print(wires)
	print(instructions)
	out = []
	i = 0
	while True:
		key = "z" + str(i).rjust(2, "0")
		if key not in instructions: break # go till z12
		s = solve(key)
		out.append(s)
		print(f"for key {key} s is {s}")
		i += 1

	print("out ",int("".join(map(str, out[::-1])),2))


	pass
def part2():
	pass

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")

	part1(data)
	part2()




