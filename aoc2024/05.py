from collections import defaultdict, deque

file = "eg.txt"
file = "in.txt"
data = open(file, "r").read().split("\n")


# This is like topological sorting
# except not really; it never points out that there is a specific entry point
# just make sure of the ordering bro 
# correct way to do part 2 is topological sort not bogo sort XD

# not in use 
def same_ordered(qq, ordered):
	# print('qq and ordered ', qq, ordered)
	if len(qq) > len(ordered):
		return False
	i = 0
	j = 0
	while i < len(qq) and j < len(ordered):
		if qq[i] == ordered[j]:
			i += 1
			j += 1
		else:
			j += 1

	return i == len(qq)

def part1(queries, orders):

	ans = 0
	for qq in queries:
		ok = True
		for q in range(len(qq)-1):
			a,b = qq[q], qq[q+1]
			if (a,b) not in orders:
				print(qq)
				ok = False
				break
		if ok:
			n = len(qq)
			mid = n//2 # so they are always odd number of inputs ??
			ans += qq[mid]
	return ans


def getRightOrder(query, orders):
	# sort the query according to orders
	for j in range(len(query)): # so sorry 🤡
		i = 0
		while i < len(query)-1:
			a, b = query[i], query[i+1]
			if (a, b) in orders or (b, a) not in orders:
				i += 1
				continue
			if (b,a) in orders: # one time sort is not enough
				query[i], query[i+1] = b, a
				i += 1
				continue 
			else:
				print('this should not happen')

	n = len(query)
	mid = n//2
	return query[mid]


def part2(queries, orders):
	print(queries)
	ans = 0
	for qq in queries:
		for q in range(len(qq)-1):
			a,b = qq[q], qq[q+1]
			if (a,b) not in orders:
				ans += getRightOrder(qq, orders)
				break
	return ans

if __name__ == "__main__":	
	queries = []
	orders = set()
	for line in data:
		if "|" in line:
			u, v = map(int, line.split("|"))
			orders.add((u,v))
		elif line:
			qq = list(map(int, line.split(",")))
			queries.append(qq)	
	
	# part1(queries, orders)
	part2(queries, orders)

