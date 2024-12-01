from collections import defaultdict

# data = open('eg.txt', 'r').read().split('\n')
data = open('in.txt', 'r').read().split('\n')


def part1():	
	list_a = []
	list_b = []

	for items in data:
		a, b = map(int, items.split())
		list_a.append(a)
		list_b.append(b)

	list_a.sort()
	list_b.sort()
	ans = 0
	for a, b in zip(list_a, list_b):
		ans += abs(a - b)
	print(ans)

def part2():
	list_a = []
	list_b = defaultdict(int)

	for items in data:
		a, b = map(int, items.split())
		list_a.append(a)
		list_b[b] += 1

	ans = 0
	for a in list_a:
		ans += list_b[a] * a
	print(ans)	

# part1()
part2()
