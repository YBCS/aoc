from collections import defaultdict, deque
dirs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left


DP = {}
def solve(design, patterns):
	# can design be made using one of the patterns
	# brwrr, [br,wr,r]
	# print('solve params ', design, patterns)

	# patters in set I should use that instead of str.startswith
	if not design: return True
	if design in DP: return DP[design]

	for pattern in patterns:
		if design.startswith(pattern) and solve(design[len(pattern):], patterns):
			DP[design] = True
			return True
	DP[design] = False
	return False

def solveII(design, patterns, DP):
	# I tried to generate all the paths but the solution I came up with had weird structure and was hard to memoize and also parse the output
	# so just the nums 
	if not design:
		DP[design] = 1 
		return 1
	if design in DP: return DP[design]

	a = 0
	for pattern in patterns:
		if design.startswith(pattern):
			a += solveII(design[len(pattern):], patterns, DP)

	if a > 0:
		DP[design] += a
		return DP[design]
	else:
		DP[design] = 0
		return 0

DP = {}
# jonathan paulson's solution
def solveII(design, patterns):
	if design in DP: return DP[design]
	
	ans = 0		
	if not design:
		ans = 1

	for pattern in patterns:
		if design.startswith(pattern):
			ans += solveII(design[len(pattern):], patterns)

	DP[design] = ans
	return ans


def part1(patterns, designs):
	patterns = set(patterns)
	print(patterns)
	print(designs)
	ans = 0
	
	for design in designs:
		if solve(design, patterns):
			ans += 1
	print('ans is ', ans)

def part2(patterns, designs):
	patterns = set(patterns)
	ans = 0
	# DP = defaultdict(int)
	# a = solveII("gbbr", patterns, DP)
	# print("asdgas ", a)
	for design in designs:
		DP = defaultdict(int)
		# ans += solveII(design, patterns, DP)
		ans += solveII(design, patterns)
	print('ans is ', ans)

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n\n")
	patterns = map(str.strip, data[0].split(','))
	designs = data[1].split('\n')

	# part1(patterns, designs)
	part2(patterns, designs)




