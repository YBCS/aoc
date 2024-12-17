from collections import defaultdict, deque


def part1(data):
	# we have a grid
	grid = []
	dirs = ""
	for line in data:
		if line and line[0] == "#":
			# grid input
			line = list(line)
			grid.append(line)

		elif line:
			# dirs input
			dirs += line
	start = None
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "@":
				start = (i,j)
				break
		if start: break

	[print(row) for row in grid]

	def move_grid(x, y, dx, dy):
		print("move_grid ", x, y, dx, dy)
		# wall 	--> cannot move
		# . 	--> move 
		# O 	--> check the next if we can move
		tx, ty = dx, dy
		# dx, dy = 0, 1
		block = False
		while grid[x+dx][y+dy] == "O":
			print("eval O ")
			block = True
			dx, dy = dx + tx, dy + ty

		# x+dx is now on . or #

		# if grid[x+dx][y+dy] == "#":
		# 	return x, y

		if grid[x + dx][y + dy] == ".":
			print("eval . ", x+dx, y+dy, grid[x+dx][y+dy])
			grid[x][y] = "."
			grid[x+tx][y+ty] = "@"
			if block:
				grid[x+dx][y+dy] = "O"

			x = x+tx
			y = y+ty

		return x, y

	x, y = start
	print("start ", x, y)
	for mov in dirs:
		if mov == "^":
			x , y = move_grid(x, y, -1, 0)
		elif mov == "v":
			x , y = move_grid(x, y, 1, 0)
		elif mov == ">":
			x , y = move_grid(x, y, 0, 1)
		elif mov == "<":
			x , y = move_grid(x, y, 0, -1)

		print('dir ', mov)
		# [print(row) for row in grid]
	ans = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "O":
				ans += (100 * i) + j
	print("ans is ", ans)

def part2(data):
	grid = []
	dirs = ""
	for line in data:
		if line and line[0] == "#":
			new_row = []
			for i in range(len(line)):
				if line[i] == "#":
					new_row.append("#")
					new_row.append("#")
				if line[i] == "O":
					new_row.append("[")
					new_row.append("]")
				if line[i] == ".":
					new_row.append(".")
					new_row.append(".")
				if line[i] == "@":
					new_row.append("@")
					new_row.append(".")

			grid.append(new_row)
		elif line:
			dirs += line

	start = None
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "@":
				start = (i,j)
				break
		if start: break

	[print(row) for row in grid]
	# TODO : refactor for part 2 
	def move_grid(x, y, dx, dy):
		# print("move_grid ", x, y, dx, dy)
		# wall 	--> cannot move
		# . 	--> move 
		# [] 	--> check the next if we can move
		tx, ty = dx, dy
		block = False
		while grid[x+dx][y+dy] in ["[", "]"]:
			print("eval [ ] ")
			block = True
			dx, dy = dx + tx, dy + ty

		if grid[x + dx][y + dy] == ".":
			# print("eval . ", x+dx, y+dy, grid[x+dx][y+dy])
			grid[x][y] = "."
			grid[x+tx][y+ty] = "@"
			if block:
				grid[x+dx][y+dy] = "O"

			x = x+tx
			y = y+ty

		return x, y

	x, y = start
	for mov in dirs:
		if mov == "^":
			x , y = move_grid(x, y, -1, 0)
		elif mov == "v":
			x , y = move_grid(x, y, 1, 0)
		elif mov == ">":
			x , y = move_grid(x, y, 0, 1)
		elif mov == "<":
			x , y = move_grid(x, y, 0, -1)

		print('dir ', mov)
		[print(row) for row in grid]
	ans = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "O":
				ans += (100 * i) + j
	print("ans is ", ans)

if __name__ == "__main__":	
	file = "in.txt"
	file = "eg.txt"
	data = open(file, "r").read().split("\n")


	# part1(data)
	part2(data)
	print()
	print()
	print()
	print()




