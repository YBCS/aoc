# day 16
# Reindeer Maze

from collections import defaultdict, deque
import heapq

def get_dirs(curr_dir):
	if curr_dir == ">":
		return [">", "^", "v"]
	if curr_dir == "<":
		return ["<", "^", "v"]
	if curr_dir == "^":
		return ["^", ">", "<"]
	if curr_dir == "v":
		return ["v", ">", "<"]
	print("no match ")

def part1(grid, start, end):
	# I think my issue is with syncing states;
	# too much states; there should be but one state and everything should derieve from it
	def move(i, j, c_dir, nx_dir, path): # x,y curr and next 
		if i == end[0] and j == end[1]: 
			print("reached the end ", path)
			return 0
		if (i, j, c_dir, nx_dir) in visited: return float('inf')
		if grid[i][j] == "#": return float('inf')
		visited.add((i,j, c_dir, nx_dir))
		ans = float('inf')
		for n_dir in get_dirs(c_dir):
			di, dj = look_up[n_dir]
			ans = min(move(i+di,j+dj,nx_dir, n_dir, path + c_dir), ans)
		return 1 + ans if c_dir == nx_dir else 1000 + ans

	look_up = {
	">": (0,1),
	"<": (0,-1),
	"^": (-1,0),
	"v": (1,0)
	}
	visited = set()
	print("start is ", start)
	print("end is ", end)
	x, y = start
	# return min(move(i,j, ">", ">", ""), move(i,j, ">", "<", ""), move(i,j, ">", "^", ""))
	return move(x,y,">",">", "")

def part1_sol(grid, start, end):
	# referenced jonathan paulson
	# I misunderstood the problem 🤡; its dijkstra's
	queue = []
	visited = set()
	dirs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
	heapq.heappush(queue, (0, start[0], start[1], 1)) # score, i, j, dir

	while queue:
		score, r, c, d = heapq.heappop(queue)
		if r == end[0] and c == end[1]:
			print("the score ", score)
			break
		if (r,c,d) in visited: continue
		visited.add((r,c,d))
		dr, dc = dirs[d]
		if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc] != "#": # why do we need to check bounds here ?
			heapq.heappush(queue, (score+1, r+dr, c+dc, d))
		heapq.heappush(queue, (score+1000, r, c, (d+1)%4)) # what's up with this d+1... woah 🤯😧
		heapq.heappush(queue, (score+1000, r, c, (d+3)%4)) # what's up with this d+3
	print('finish ')



def part2():
	pass

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")
	grid = []
	start, end = None, None
	row, col = len(data), len(data[0])
	for i in range(row):
		line = list(data[i])
		grid.append(line)
		for j in range(col):
			if line[j] == "E":
				end = (i,j)
			if line[j] == "S":
				start = (i,j)
	
	# ans = part1(grid, start, end)
	# print('ans is ', ans)
	part1_sol(grid, start, end)





