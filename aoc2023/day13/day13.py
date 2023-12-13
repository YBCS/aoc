# aoc day 13
data = open('input.txt', 'r').read().split('\n')


def is_rows_equal(r1, r2, mat):
	for col in range(len(mat[0])):
		if mat[r1][col] != mat[r2][col]:
			return False
	return True

def is_cols_equal(c1, c2, mat):
	for row in range(len(mat)):
		if mat[row][c1] != mat[row][c2]:
			return False
	return True

def get_vertical_mirror_point(mat): # |
	for col in range(1, len(mat[0])):
		foundOne = True
		for row in range(len(mat)):
			if mat[row][col] != mat[row][col-1]:
				foundOne = False
				break
		if foundOne:
			left = col - 1
			right = len(mat[0]) - col - 1
			span = min(left, right)
			foundAll = True
			for i in range(span):
				if not is_cols_equal(col-i-2, col+i+1, mat):
					foundAll = False
					break
			if foundAll:
				return col
	return -1

def get_horizontal_mirror_point(mat): # -----
	for row in range(1, len(mat)):
		foundOne = True
		for col in range(len(mat[0])):
			if mat[row][col] != mat[row-1][col]:
				foundOne = False
				break
		if foundOne:
			# check the others too
			up = row - 1
			down = len(mat) - row - 1
			span = min(up, down)
			# do the same check for the entire span
			foundAll = True
			for i in range(span):
				if not is_rows_equal(row-i-2, row+i+1, mat):
					foundAll = False
					break
			if foundAll:
				return row
	return -1

def part1(data):
	mat = []
	ans = 0
	for row in data:
		if row: 
			mat.append(row)
		else:
			print()
			[print(r) for r in mat]
			v = get_vertical_mirror_point(mat) # |
			print('mirror vertically | at ', v)
			if v>0: ans += v

			h = get_horizontal_mirror_point(mat) # ----
			print('mirror horizontally ---- at ', h)
			if h>0: ans += 100*h
			mat = [] # reset; new input
	print(ans)
	return ans


def part2(data):
	'''
	# seems doable
	for each mat
		## find "new" mirror point:
			# find the smudge:
				it is a point which if changed; makes it a valid mirror point
		### use new mirror point to calculate ans
	'''
	pass

part1(data) # 35538
# part2(data)
