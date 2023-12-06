# aoc day 6

data = open('input.txt', 'r').read().split('\n')

def part1(data):
	print(data)
	time, distance = data[0].split(':')[1].strip().split(' '), data[1].split(':')[1].strip().split(' ')
	time = [int(t) for t in time if t]
	distance = [int(d) for d in distance if d]

	ans = 1
	for i in range(len(time)):
		t, d = time[i], distance[i]	
		success = 0
		for i in range(1, t):
			if i*(t-i) > d:
				success += 1
		ans *= success
		# print('success is ', success)
	print(ans)

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


part2(data)