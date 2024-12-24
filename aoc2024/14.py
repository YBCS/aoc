from collections import defaultdict, deque


class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Operands must be of type Vector")
		return Vector(self.x + other.x, self.y + other.y)

	def is_overlapping(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Operands must be of type Vector")
		return self.x == other.x and self.y == other.y

	def __repr__(self):
		return f"Vector(x={self.x}, y={self.y})"

def print_grid_util(pos, w, h):
	print('pos ', pos)
	grid = [["."]*w for _ in range(h)]
	for vec in pos:
		grid[vec.y][vec.x] = 'A'
	[print(row) for row in grid]

def part1(data):
	width, height = 11, 7
	width, height = 101, 103

	POS_VEL = []
	for line in data:
		pos, vel = line.split(" ")
		pos, vel = list(map(int, pos[2:].split(','))), list(map(int, vel[2:].split(',')))
		pos_vec = Vector(pos[0], pos[1])
		vel_vec = Vector(vel[0], vel[1])
		POS_VEL.append((pos_vec, vel_vec))

	iters = 5
	iters = 100
	for i in range(iters):
		NEW_POS_VEL = []
		for pos, vel in POS_VEL:

			new_pos = pos + vel
			if new_pos.x >= width:
				new_pos.x = new_pos.x - width
			elif new_pos.x < 0:
				new_pos.x = width + new_pos.x

			if new_pos.y >= height:
				new_pos.y = new_pos.y - height
			elif new_pos.y < 0:
				new_pos.y = height + new_pos.y
			NEW_POS_VEL.append((new_pos, vel))
		POS_VEL = NEW_POS_VEL


	mid_height, mid_width = height // 2, width // 2
	pos = [pos for pos, vel in POS_VEL]
	filetered = []
	for p in pos:
		if p.x == mid_width: continue
		if p.y == mid_height: continue
		filetered.append(p)

	ans = 1
	Q1 = defaultdict(int) # quadrants
	Q2 = defaultdict(int)
	Q3 = defaultdict(int)
	Q4 = defaultdict(int)

	for i in range(len(filetered)):
		pos = filetered[i]
		x, y = pos.x, pos.y
		if x < mid_width and y < mid_height: # Q1
			Q1[(x,y)] += 1
		if x < mid_width and y > mid_height: # Q2
			Q2[(x,y)] += 1
		if x > mid_width and y < mid_height: # Q3
			Q3[(x,y)] += 1
		if x > mid_width and y > mid_height: # Q3
			Q4[(x,y)] += 1


	for Q in [Q1, Q2, Q3, Q4]:
		ans *= sum(Q.values())
	print('ans ', ans)


def part2():
	## or just look for xxxxxxx :D
	# try no of floating islands
	# the answer probably has less islands
	# print them out and check; it wants the iteration number
	# can u print out a frame of the input
	pass

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")
	part1(data)
