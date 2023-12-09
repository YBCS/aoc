# aoc day 8

data = open('input.txt', 'r').read().split('\n')

def part1(data):
	direction = data[0]
	data = data[2:]
	store = {}
	
	for d in data:
		k, v = d.split(" = ")
		k.strip()
		v.strip()
		l, r = v.split(", ")
		l = l[1:] # there has to be cleaner way to remove those parenthesis
		r = r[:-1]
		store[k] = [l, r]
	
	# [print(k,v) for k,v in store.items()]

	key = "AAA"
	count = 0
	while True:
		for d in direction:
			count += 1
			d = 0 if d == "L" else 1
			if store[key][d] == "ZZZ":
				print(f"found zzz in {count} steps")
				return count
			key = store[key][d]

def part2(data):
	direction = data[0].strip()
	print(direction)
	data = data[2:]
	store = {}
	
	for d in data:
		k, v = d.split(" = ")
		k.strip()
		v.strip()
		l, r = v.split(", ")
		l = l[1:] # there has to be cleaner way to remove those parenthesis
		r = r[:-1]
		store[k] = [l, r]
	
	# [print(k,v) for k,v in store.items()]

	keys = [k for k in store if k[-1] == "A"]
	loops = []
	for key in keys:
		count = 1
		i = 0
		
		item = key
		d = 0 if direction[i] == "L" else 1
		while store[item][d][-1] != "Z":
			count += 1
			print(f"from {item}")
			print(f"to {store[item][d]}")
			item = store[item][d]
			i += 1
			if i >= len(direction): i = 0
			d = 0 if direction[i] == "L" else 1
			print()
		# here store[item][d] has reached Z
		loops.append(count)
	
	print(f"loops {loops}")


# NOTE: no lol; please calculate lcm instead # add implementation
def multiplyAll(items):
	ans = 1
	for item in items:
		ans *= item
	print(f"ans is {ans}")
	return ans

multiplyAll([16343, 16897, 20221, 18559, 11911, 21883])
# 27011809034838424525673297 # too high ?
# 16,563,603,485,021

part2(data)
