# aoc day 12
data = open('input.txt', 'r').read().split('\n')

# NOTE : incomplete
def part1(data):
	print(data)
	for d in data:
		springs, numbers = d.split(' ')
		numbers = list(map(int, numbers.split(',')))
		print(springs, numbers)

#/*****************************************************************************/
# by jonathan paulson
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/12.py
# this is a dp problem so don't feel too bad; you should be able to do this once you've practised some dp 
def is_valid(dots, blocks): # dots: ".###.##.#..." blocks = [3, 2, 1] ; returns true
	# print('is valid called ', dots, blocks)
	current = 0
	seen = []
	for c in dots:
		if c == ".":
			if current > 0:
				seen.append(current)
			current = 0
		elif c == "#":
			current += 1
		else: # should not reach
			assert False
	if current > 0: # the last one in iter
		seen.append(current)
	return seen == blocks


def f(dots, blocks, i):
	if i == len(dots): # check
		# return 1 if is_valid(dots, blocks) else 0
		return 1 if is_equal(dots, blocks) else 0
	if dots[i] == '?': # where ever there is a ? ; try # or .
		return (f(dots[:i]+"#"+dots[i+1:], blocks, i+1) + 
				f(dots[:i]+"."+dots[i+1:], blocks, i+1))
	else:
		return f(dots, blocks, i+1)

def solution(data):
	ans = 0
	for d in data:
		dots, blocks = d.split()
		blocks = list(map(int, blocks.split(',')))
		score = f(dots, blocks, 0)	
		print(dots, blocks, score)
		# print(is_valid('#.#.###', [1,1,3]))
		ans += score
	print(ans)
#/*****************************************************************************/


# this is mine :)
def is_equal(dots, blocks):
	dots = dots.split('.')
	dots = [d for d in dots if d]
	dots = [len(d) for d in dots]
	return dots == blocks

# part1(data)
solution(data)



