from collections import defaultdict, deque

import math

def part1(data):
	# part 2 is how fast I can do this
	blinks = 75
	print('data is ', data)
	out = []
	for _ in range(blinks):
		out = []
		for num in data:
			if num == "0": # replace with 1 
				num = "1"
			elif len(num) % 2 == 0: # if even count --> break in half and 
				i = len(num) // 2
				l = num[:i]
				r = num[i:]
				out.append(l)
				out.append(str(int(r)))
				continue
			else: # odd count --> multiply by 2024
				num = str(int(num) * 2024)

			out.append(num)
		data = out
		# print('out is ', out)
	print('ans is ', len(out))

def count_num(num):
	return 1 if num == 0 else int(math.log10(num)) + 1

def break_two(num, n):
	# print('args ', num, n)
	num1 = num // (10**n)
	num2 = num % (10**n)
	return [num1, num2]

def part2(data, cache):
	# observation : order does not matter
	# and this operaiton will cause repetitions
	# use counts 
	data = list(map(int, data))
	print('part 2 data ', data)
	blinks = 75
	out = []
	for _ in range(blinks):
		print("_ ", _)
		out = []
		for num in data:
			temp = num
			if num in cache:
				out.extend(cache[num])
				continue
			
			n = count_num(num)
			if num == 0: # replace with 1 
				num = 1
			elif n % 2 == 0: # if even count --> break in half and 
				a = break_two(num, n//2)
				out.extend(a)
				cache[temp] = a
				continue
			else: # odd count --> multiply by 2024
				num = num * 2024

			cache[temp] = [num]
			out.append(num)
		data = out
	print('ans is ', len(out))


def part2II(data, cache):
	# observation : order does not matter
	# and this operaiton will cause repetitions
	# use counts 

	data = list(map(int, data))
	blinks = 6

	for num in data:
		cache[num] += 1

	for _ in range(blinks):

		print("_ ", _)
		for num in data:
			temp = num
			# if num in cache:
			# 	out.extend(cache[num])
			# 	continue

			n = count_num(num)
			if num == 0: # replace with 1 
				num = 1
			elif n % 2 == 0: # if even count --> break in half and 
				a = break_two(num, n//2)
				continue
			else: # odd count --> multiply by 2024
				num = num * 2024

	print('ans is ', len(out))

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")[0]
	data = data.split(" ")

	# print(count_num(0))
	# print(break_two(253000, 3))
	# part1(data)
	part2(data, defaultdict(int))




