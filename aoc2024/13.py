from collections import defaultdict, deque


# DP: from jonathan paulson
def solve(A_x, A_y, B_x, B_y, Prize_x, Prize_y):
	DP = {}
	def fn(x, y):
		if (x,y) in DP: return DP[(x,y)]
		if x == 0 and y == 0: return 0
		if x < 0 or y < 0: return float('inf')
		ans = min(3+fn(x-A_x, y-A_y), 1+fn(x-B_x, y-B_y))
		DP[(x,y)] = ans
		return ans
	ans = fn(Prize_x, Prize_y)
	# how did this 1000 come ? -> 400 coz 3*100 + 1*100
	return ans if ans < 400 else 0


def part1(data):
	ans = 0
	for test in data:
		query = test.split('\n')
		A, B, Prize = query
		A_x, A_y = A[10:].split(",")
		A_x, A_y = int(A_x[2:]), int(A_y[2:])

		B_x, B_y = B[10:].split(",")
		B_x, B_y = int(B_x[2:]), int(B_y[2:])

		Prize_x, Prize_y = Prize[7:].split(", ")
		Prize_x, Prize_y = int(Prize_x[2:]), int(Prize_y[2:])

		ans += solve(A_x, A_y, B_x, B_y, Prize_x, Prize_y)

	print('ans is ', ans)


def part2():
	pass

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n\n")

	part1(data)
	# part2()




