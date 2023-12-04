
data = open('input.txt', 'r').read().split('\n')

def part1(data):
	# print('data ', data)
	ans = 0
	for card in data:
		card = card.split(':')[1].strip()
		front, back = card.split('|')
		front = front.split(' ')
		back = back.split(' ')
		front_set = set()
		for num in front:
			if num.isdigit(): # can be done with map easier
				front_set.add(num)
		back_set = set()
		for num in back:
			if num.isdigit(): # can be done with map easier
				back_set.add(num)
		intersection = back_set.intersection(front_set)
		intersection_len = len(intersection)
		if intersection_len:
			ans += 2**(intersection_len-1)

	print(f'ans is {ans}')

def part2(data):
	ans = 0
	game_to_intersection = {}
	card_instances = {}
	for i, card in enumerate(data):
		card_instances[i+1] = 1
		card = card.split(':')[1].strip()
		front, back = card.split('|')
		front = front.split(' ')
		back = back.split(' ')

		front_set = set()
		for num in front:
			if num.isdigit():
				front_set.add(num)
		back_set = set()
		for num in back:
			if num.isdigit(): # can be done with map easier
				back_set.add(num)
		intersection = back_set.intersection(front_set)
		intersection_len = len(intersection)
		game_to_intersection[i+1] = intersection_len

	# print(f'game_to_intersection {game_to_intersection}')
	# print(f'card_instances {card_instances}')
	# print()
	# processing # there is a bug here and idk where 
	for i in range(len(card_instances)):
		start = 0
		end = 0
		for _ in range(card_instances[i+1]):
			start = i+2
			end = min(len(card_instances)+1, start+game_to_intersection[i+1]) # here lies the bug : len(card_instances)+1 ; I forgot the +1
			for j in range(start, end):
				card_instances[j] += 1

	# 	print(f'start {start} and end {end}')
	# 	print('card_instances ', card_instances)
	
	# print()
	# print('final card_instances ', card_instances)
	print(f'ans is {sum(card_instances.values())}')

# 5743562 too low
# 5747443 

part2(data)
