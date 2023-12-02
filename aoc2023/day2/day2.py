from collections import deque

data = open('input.txt', 'r').read().split('\n')
# 12 red cubes, 13 green cubes, and 14 blue cubes

def part1(data):
	ans = 0
	COLOR = {"blue": 14, "red": 12, "green": 13}
	for i, games in enumerate(data):
		
		games = games.split(':')[1]
		games = games.split(';')
		# print(i+1, games)
		for game in games:
			flag = True
			each_game = game.split(',')
			for g in each_game:
				count, color = g.split(' ')[1], g.strip()[2:]
				if COLOR[color.strip()] < int(count):
					flag = False
					break
			if not flag: break

		game_id = i+1
		if flag: ans += game_id


def part2(data):
	ans = 0
	for i, games in enumerate(data):
		games = games.split(':')[1]
		games = games.split(';')
		COLOR = {"blue": 0, "red": 0, "green": 0}
		for game in games:
			each_game = game.split(',')
			for g in each_game:
				count, color = int(g.split(' ')[1]), g.strip()[2:]
				COLOR[color.strip()] = max(COLOR[color.strip()], count)
		print(COLOR)
		curr = 1
		for count in COLOR.values():
			curr *= count
		ans += curr
	print('ans is ', ans)


part2(data)
