from collections import defaultdict, deque
dirs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

def part1(data):
	# straightforward --> shortest path; bfs; dijkstra's
	row, col = 6, 6
	row, col = 70, 70
	amt = 12
	amt = 1024

	blocks = set()
	for line in data[:amt]:
		x, y = map(int, line.split(','))
		print(x,y)
		blocks.add((x,y))

	sr, sc = 0,0 # x y -> x is col, y is row
	er, ec = row, col

	queue = deque([(sr, sc, 0)])
	visited = set()
	while queue:
		x, y, score = queue.popleft()
		if x == ec and y == er:
			print('the score is ', score)
			break
		if not (0<=x<=col) or not (0<=y<=row): continue
		if (x,y) in blocks: continue
		if (x,y) in visited: continue
		print("in queue ", x, y, score)

		visited.add((x,y))
		for dx, dy in dirs:
			queue.append((x+dx,y+dy,score+1))

def part2(data):
	row, col = 6, 6
	row, col = 70, 70
	amt = 12
	amt = 1024

	blocks = set()
	for line in data[:amt]:
		x, y = map(int, line.split(","))
		blocks.add((x,y))

	sr, sc = 0,0 # x y -> x is col, y is row
	er, ec = row, col


	amt_ptr = amt
	while True:
		nx, ny = map(int, data[amt_ptr].split(","))
		blocks.add((nx, ny))
		amt_ptr += 1
		# detect that this is not halting; wow the halting problem
		# but in this case we know the grid size

		queue = deque([(sr, sc, 0)])
		visited = set()
		reached_end = False
		while queue:
			x, y, score = queue.popleft()
			if x == ec and y == er:
				reached_end = True
				break
			if not (0<=x<=col) or not (0<=y<=row): continue
			if (x,y) in blocks: continue
			if (x,y) in visited: continue

			visited.add((x,y))
			for dx, dy in dirs:
				queue.append((x+dx,y+dy,score+1))

		print('reached end status ', reached_end)
		print("the new block ", nx, ny)
		if not reached_end:
			print("blocked by ", nx, ny)
			print("pos of ", amt_ptr)
			break


if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")


	# part1(data)
	part2(data)




