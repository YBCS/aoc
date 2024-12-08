file = "eg.txt"
file = "in.txt"
data = open(file, "r").read().split("\n")


def is_equate_pipe(nums, total):
	# can the nums operated on +, *, || make the total 
	Q = [(nums[0], '+', 1), (nums[0], '*', 1), (nums[0], '||', 1)] # (total, operator, index)
	n = len(nums)
	while Q:
		T, O, i = Q.pop()
		if i == n:
			if T == total:
				return True
			continue
		a, b = T, nums[i]
		if O == "+":
			T = a + b
		if O == "*":
			T = a * b
		if O == "||":
			T = int(str(a) + str(b))
		Q.append((T, '+', i+1))
		Q.append((T, '*', i+1))
		Q.append((T, '||', i+1))
	return False

def is_equate(nums, total):
	# can the nums operated on +, * make the total
	Q = [(nums[0], '+', 1), (nums[0], '*', 1)] # (total, operator, index)
	n = len(nums)
	while Q:
		T, O, i = Q.pop()
		if i == n:
			if T == total:
				return True
			continue
		a, b = T, nums[i]
		if O == "+":
			T = a + b
		if O == "*":
			T = a * b
		Q.append((T, '+', i+1))
		Q.append((T, '*', i+1))
	return False

def part1():
	ans = 0
	for line in data:
		line = line.split(" ")
		total = int(line[0][:-1])
		nums = list(map(int, line[1:]))
		if is_equate(nums, total):
			ans += total

	print('ans ', ans)


def part2():
	ans = 0
	for line in data:
		line = line.split(" ")
		total = int(line[0][:-1])
		nums = list(map(int, line[1:]))
		if is_equate_pipe(nums, total):
			print('worked ', total, nums)
			ans += total

	print('ans ', ans)

# part1()
part2()