# data = open('eg.txt', 'r').read().split('\n')
data = open('in.txt', 'r').read().split('\n')

def is_safe(items):
	# items is a list of numbers
	# 1) it should be inc or dec
	# 2) gap is defined

	for i in range(1, len(items)):
		a, b = items[i-1], items[i]
		diff = abs(a - b)
		if diff < 1 or diff > 3:
			return False
	
	if sorted(items) == items: return True
	if sorted(items, reverse=True) == items: return True

	return False

# not in use
def is_safe_II(items):
	# if removing one item makes it okay

	for i in range(1, len(items)):
		a, b = items[i-1], items[i]
		diff = abs(a - b)
		if diff < 1 or diff > 3:
			return False
	
	if sorted(items) == items: return True
	if sorted(items, reverse=True) == items: return True

	return False


def part1():
	safe = 0
	for items in data:
		items = list(map(int, items.split()))
		if is_safe(items):
			safe += 1
	print(safe)

def part2():
	safe = 0
	for items in data:
		items = list(map(int, items.split()))
		# try removing one from all of them and check if even one is enough
		if is_safe(items):
			safe += 1
		else:
			for i in range(len(items)):
				new_item = []
				for j in range(len(items)):
					if i != j:
						new_item.append(items[j])
				if is_safe(new_item):
					safe += 1
					break
	print(safe)

# part1()
part2()
