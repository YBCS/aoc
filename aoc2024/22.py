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

def mix(value, sn):
	return value ^ sn

def prune(sn):
	return sn % 16777216

def next_sn(sn):
	# this is in no way slow but...
	temp = sn
	a = sn * 64
	b = mix(sn, a)
	sn = prune(b)

	a = sn // 32
	b = mix(sn, a)
	sn = prune(b)

	a = sn * 2048
	b = mix(sn, a)
	sn = prune(b)

	# print(f"input {temp} output {sn}")
	return sn
	
def part1(data):
	out = 0
	for line in data:
		sn = int(line)
		for _ in range(2000):
			sn = next_sn(sn)
		out += sn

		print(f"input {line} output {sn}")
	print("out ", out)

def part2(data):
	candidates = []
	price_change_all = []

	for sn in data:
		sn = int(sn)

		change = None
		prev = 0
		max_price = sn % 10
		price_change = [(max_price, None)]

		# for _ in range(2000):
		for _ in range(10):
			price = sn % 10
			temp = sn
			sn = next_sn(sn)
			if change is None:
				prev = price
				change = 0
				continue
			else:
				change = price - prev
				prev = price

			price_change.append((price, change))
			max_price = max(max_price, price)
			# print(f"input {temp} \t price {price} \t change {change}")

		price_change_all.append(price_change)
		# print(price_change)
		# print(max_price)

		# find biggest and its index
		print("max price is ", max_price)
		candidate = []
		for i in range(len(price_change)):
			price, change = price_change[i]
			if price == max_price:
				if i >= 4: # TODO: is this safe
					candidate = price_change[i-3:i+1]
					candidates.append(tuple(change for price, change in candidate))
					break

	print("price cahnge all ", price_change_all)
	# print("price change all ")
	# for price_change in price_change_all:
	# 	for price, change in price_change:
	# 		print("price ", price)
	# 	print()


	# return
	# [print(pc) for pc in price_change_all]
	# process the candidate
	# print("changes ", changes)
	# candidates = [(-2,1,-1,3)]
	print("candidates gen ?? ", candidates)
	return
	best = float("-inf")
	prices = []
	for candidate in candidates:
		ans = 0
		price_unit = []
		for price_change in price_change_all:
			n = len(price_change)
			for i in range(n):
				if i + 3 < n: # 0 1 2 3
					price, change1 = price_change[i]
					price, change2 = price_change[i+1]
					price, change3 = price_change[i+2]
					price, change4 = price_change[i+3]

					if candidate == (change1, change2, change3, change4):
						ans += price
						price_unit.append(price)
						# print("the price found ", price)
		prices.append(price_unit)
		# print()

		best = max(best, ans)

	print("prices are ", prices)
	print("best is ", best)


def part2(data):
	print('sol ')
	# solution ref: Hyperneutrino
	candidates = {}

	for sn in data:
		sn = int(sn)

		change = None
		prev = 0
		price_change = [(sn % 10, None)]

		for _ in range(2000):
			price = sn % 10
			temp = sn
			sn = next_sn(sn)
			if change is None:
				prev = price
				change = 0
				continue
			else:
				change = price - prev
				prev = price

			price_change.append((price, change))

		# print(price_change)
		seen = set()
		for i in range(len(price_change)-3):
			# 012345
			price, change1 = price_change[i]
			price, change2 = price_change[i+1]
			price, change3 = price_change[i+2]
			price, change4 = price_change[i+3]
			candidate = (change1, change2, change3, change4)
			if candidate in seen: continue
			# print("can")
			seen.add(candidate)
			if candidate not in candidates:
				candidates[candidate] = 0
			candidates[candidate] += price

	print("ans ", max(candidates.values()))





if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")

	# part1(data)
	part2(data)

