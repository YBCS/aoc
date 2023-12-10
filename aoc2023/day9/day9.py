# aoc day 9

data = open('input.txt', 'r').read().split('\n')

def part1(data):
	ans = 0
	for histories in data:
		# print(histories)
		curr_histories = list(map(int, histories.split(' ')))
		last_history = [curr_histories[-1]]
		isAllSame = False
		while not isAllSame:
			diffs, isAllSame = getDiffs(curr_histories)
			last_history.append(diffs[-1])
			curr_histories = diffs
		# print(f"last histories {last_history}")
		ans += sum(last_history)
	print(ans)

				

# returns the diffs array and isAllSame
def getDiffs(items): # ughhhh 
	 # NOTE : every one seems to notice this can be solved cleanly recursively, so implement that too
	diffs = []
	prev = items[0]
	isAllSame = True
	for i, item in enumerate(items):
		if i > 0:
			diff = item - prev
			if i > 1 and diff != diffs[-1]:
				isAllSame = False
			diffs.append(diff)
		prev = item
	# print(diffs, isAllSame)
	# print()
	return diffs, isAllSame


def part2(data):
	ans = 0
	for histories in data:
		curr_histories = list(map(int, histories.split(' ')))
		first_history = [curr_histories[0]] # this time it will be bottom up
		isAllSame = False
		while not isAllSame:
			diffs, isAllSame = getDiffs(curr_histories)
			first_history.append(diffs[0])
			curr_histories = diffs
		acc = 0
		for curr in reversed(first_history):
			acc = curr - acc
		ans += acc
	print(ans)

part2(data)
# test = [1,3,6,10,15,21]
# test = [0,3 ,6, 9, 12, 15]
# print(getDiffs(test))


# 1:20 mins 😓