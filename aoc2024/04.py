# file = "eg.txt"
file = "in.txt"
data = open(file, "r").read().split("\n")


key = "XMAS"
n = len(data)
m = len(data[0])


def getXMAS(i, j):
	# XMAS
	out = 0
	if j+3 < m and data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
		# right side 
		out += 1
	
	# SAMX
	if j-3 >= 0 and data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
		# left
		out += 1

	if i+3 < n and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
		# bottom
		out += 1

	if i-3 >= 0 and data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
		# up
		out += 1

	# diagonals
	# bottom-right
	if i+3 < n and j+3 < m and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
		out += 1
	# bottom-left
	if i+3 < n and j-3 >= 0 and data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
		out += 1
	# up-right
	if i-3 >= 0 and j+3 < m and data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
		out += 1
	# up-left
	if i-3 >= 0 and j-3 >= 0 and data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
		out += 1

	return out


print(n, m)
def X_MAS(i, j):
	# find A and alteranting diag should be M/S
	# i, j is at "A"

	# upleft to bottom right
	if (i-1 >= 0 and j-1 >=0) and (i+1 < n and j+1 < m):
		if (data[i-1][j-1] == "M" and data[i+1][j+1] == "S") or (data[i-1][j-1] == "S" and data[i+1][j+1] == "M"):
			if (data[i-1][j+1] == "M" and data[i+1][j-1] == "S") or (data[i-1][j+1] == "S" and data[i+1][j-1] == "M"):
				return 1
	
	return 0


def part1():
	# find XMAS
	# horizontal vertiacal diagonal backward overalapping

	ans = 0
	for i in range(n):
		for j in range(m):
			if data[i][j] == "X":
				ans += getXMAS(i,j)
	print(ans)


def part2():
	# find X-MAS

	ans = 0
	for i in range(n):
		for j in range(m):
			if data[i][j] == "A":
				ans += X_MAS(i,j)
	print(ans)



# part1()
part2()