from collections import defaultdict, deque


# great,linear algebra!

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Operands must be of type Vector")
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Operands must be of type Vector")
		return Vector(self.x - other.x, self.y - other.y)

	def __mul__(self, scalar):
		if not isinstance(scalar, (int, float)):
			raise TypeError("The scalar must be a number")
		return Vector(self.x * scalar, self.y * scalar)

	def __rmul__(self, scalar):
		return self.__mul__(scalar)

	def __repr__(self):
		return f"Vector(x={self.x}, y={self.y})"


def in_bounds(vec, row, col):
	return vec.x >= 0 and vec.x < col and vec.y >= 0 and vec.y < row

def getAntinodesInBounds(vec_a, vec_b, row, col):
	# parametric eqn of line is (AB*t + A); AB = B - A
	AB = vec_b - vec_a
	t1 = -1
	t2 = 2
	new_vec1 = (AB * t1) + vec_a
	new_vec2 = (AB * t2) + vec_a
	out = []
	if in_bounds(new_vec1, row, col):
		out.append((new_vec1.x, new_vec1.y))
	if in_bounds(new_vec2, row, col):
		out.append((new_vec2.x, new_vec2.y))
	return out

def getAntinodesInBoundsII(vec_a, vec_b, row, col):
	AB = vec_b - vec_a

	out = []
	
	t = -1
	new_vec = (AB * t) + vec_a
	while in_bounds(new_vec, row, col):
		out.append((new_vec.x, new_vec.y))
		t -= 1
		new_vec = (AB * t) + vec_a

	t = 2
	new_vec = (AB * t) + vec_a
	while in_bounds(new_vec, row, col):
		out.append((new_vec.x, new_vec.y))
		t += 1
		new_vec = (AB * t) + vec_a
	return out

def part1(frequencies, row, col):
	# so for reach type; do the math
	# and add to a set; count the set

	antinode = set()
	for key in frequencies:
		for i in range(len(frequencies[key])):
			for j in range(i+1, len(frequencies[key])):
				A_x, A_y = frequencies[key][i]
				B_x, B_y = frequencies[key][j]
				A = Vector(A_x, A_y)
				B = Vector(B_x, B_y)
				out = getAntinodesInBounds(A, B, row, col)
				for vec in out:
					antinode.add((vec))

	print('ans ', len(antinode))

def part2(frequencies, row, col):
	antinode = set()
	for key in frequencies:
		for i in range(len(frequencies[key])):
			for j in range(i+1, len(frequencies[key])):
				A_x, A_y = frequencies[key][i]
				B_x, B_y = frequencies[key][j]
				A = Vector(A_x, A_y)
				B = Vector(B_x, B_y)
				out = getAntinodesInBoundsII(A, B, row, col)
				for vec in out:
					antinode.add((vec))

	ans = len(antinode)

	for key in frequencies:
		for x,y in frequencies[key]:
			if (x,y) not in antinode:
				ans += 1

	print('ans ', ans)

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")

	# 12 * 12
	row = len(data)
	col = len(data[0])
	frequencies = defaultdict(list)
	for i in range(row):
		for j in range(col):
			if data[i][j] != ".":
				frequencies[data[i][j]].append((i,j))

	part1(frequencies, row, col)
	part2(frequencies, row, col)




