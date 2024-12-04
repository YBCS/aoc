# I think this can be solved very well with regex

file = "eg.txt"
file = "in.txt"
data = open(file, "r").read().split("/n")

def part1():
	# literally a small parser
	# it could be more worse if nested inputs are allowed : recursion
	for line in data:
		# lets brute this
		# find mul(
		# find next ,; things between should be int
		# find next); things between should be int
		# pass
		# else fail
		print(line)

		# mul(1,0) # 8 chars
		# mul(asgf,asgd,mul(a,b))
		n = len(line)
		ans = 0
		i = 0
		while i < n:
			num1 = 0
			num2 = 0
			if i+7 < n and line[i] == "m" and line[i: i+4] == "mul(":
				s = i+4
				e = i+4
				
				j = i+4 # mul(,,,,,)
				while j < n: # look for ,
					if line[j] == ',':
						e = j
						break
					j += 1
				if line[s:e].isnumeric():
					num1 = int(line[s:e])
				j+=1
				s = j
				e = j
				while j < n: # look for ) mul(a,b) mul(askdjg
					if line[j] == ")":
						e = j
						break
					j += 1
				if line[s:e].isnumeric():
					num2 = int(line[s:e])

				ans += num1 * num2
				print('num 1 and 2 ', num1, num2)
				i += 4
			else:
				i += 1
		print('ans is ', ans)

def part2():
	for line in data:
		n = len(line)
		ans = 0
		i = 0
		mode = True # "do"(True)|"dont"(False)
		while i < n:
			num1 = 0
			num2 = 0
			# don't() 	# 7 chars
			# do() 		# 4 chars
			if i+6 < n and line[i: i+7] == "don't()":
				mode = False
				i += 7
				continue
			if i+3 < n and line[i: i+4] == "do()":
				mode = True
				i += 4
				continue

			if i+7 < n and line[i] == "m" and line[i: i+4] == "mul(":
				s = i+4
				e = i+4
				j = i+4
				while j < n:
					if line[j] == ',':
						e = j
						break
					j += 1
				if line[s:e].isnumeric():
					num1 = int(line[s:e])
				j+=1
				s = j
				e = j
				while j < n:
					if line[j] == ")":
						e = j
						break
					j += 1
				if line[s:e].isnumeric():
					num2 = int(line[s:e])

				if mode:
					ans += num1 * num2
					print
				i += 4
			else:
				i += 1
		print(ans)

# part1()
part2()