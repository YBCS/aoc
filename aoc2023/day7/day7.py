# aoc day 7
# from functools import cmp_to_key

data = open('input.txt', 'r').read().split('\n')

# def hand_order(a, b):
# 	if a[0] > b[0]: return 1 # +ve is greater than
# 	if a[0] == b[0]: # if same count # this is where it gets tricky
# 		if a[2] > b[2]: return 1
# 		if a[2] == b[2]: return 0
# 		return -1
# 	return -1 # -ve is less than

# adapted from Jonathan Paulson: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/7.py
def getStrength(item): # sorting hands problem
	counts, hand, bid = item
	hand = hand.replace('T', chr(ord('9')+1)) # what is this doing ?
	hand = hand.replace('J', chr(ord('9')+2))
	hand = hand.replace('Q', chr(ord('9')+3))
	hand = hand.replace('K', chr(ord('9')+4))
	hand = hand.replace('A', chr(ord('9')+5))

	if(list(counts.values()) == [5]):
		return (10, hand)
	elif(sorted(counts.values()) == [1,4]):
		return (9, hand)
	elif(sorted(counts.values()) == [2,3]):
		return (8, hand)
	elif(sorted(counts.values()) == [1,1,3]):
		return (7, hand)
	elif(sorted(counts.values()) == [1,2,2]):
		return (6, hand)
	elif(sorted(counts.values()) == [1,1,1,2]):
		return (5, hand)
	elif(sorted(counts.values()) == [1,1,1,1,1]):
		return (4, hand)
	else:
		assert False, f'{counts} {hand} {sorted(counts.values())}'


def part1(data):
	# print(data)
	formatted = []
	for i in range(len(data)):
		hand, bid = data[i].split(' ')
		counter = {}
		for ch in hand:
			counter[ch] = counter.get(ch, 0) + 1
		formatted.append((counter, hand, int(bid)))
	
	# sort the formatted
	# hand_cmp_key = cmp_to_key(hand_order)
	# formatted.sort(key=hand_cmp_key)
	# formatted.sort(key=lambda item: getStrength(item))

	formatted = sorted(formatted, key=lambda item: getStrength(item))
	# [print(x) for x in formatted]
	
	# calculate the output
	ans = 0
	for i, (counts, hand, bid) in enumerate(formatted):
		# print(counts, hand, bid, i)
		ans += (i+1) * bid

	print(ans)

# 251545217	# too high

# NOTE : incomplete
def part2(data):
	time, distance = data[0].split(':')[1].strip().split(' '), data[1].split(':')[1].strip().split(' ')
	t = ""
	for _t in time:
		if _t:
			t += _t
	t = int(t)
	d = ""
	for _d in distance:
		if _d:
			d += _d
	t = int(t)	
	d = int(d)

	print(t, d)

	success = 0
	for i in range(1, t):
		if i*(t-i) > d:
			success += 1
	
	print('success is ', success)


part1(data)