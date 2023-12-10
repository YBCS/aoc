# aoc day 10

from collections import deque

data = open('input.txt', 'r').read().split('\n')

# if r-1 >= 0: # up
# 	if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
# 		start.append((r-1,c))
# 		valid += 1
# if c-1 >= 0: # left
# 	if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
# 		start.append((r,c-1))
# 		valid += 1
# if c+1 < len(data[0]): # right
# 	if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
# 		start.append((r,c+1))
# 		valid += 1
# if r+1 < len(data): # down
# 	if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
# 		start.append((r+1,c))
# 		valid += 1

### NOTE : this is my original implementation
# def part1(data):
# 	print(data)
# 	for r in range(len(data)):
# 		for c in range(len(data[0])):
# 			if data[r][c]=="S":
# 				start = deque([(r, c)])
# 				print(f"found S at {r, c}")
# 				break
# 	# lets pray there is atmost 2 valid options for each pipe
# 	i = 0
# 	visited = set((r,c))
	
# 	# need to find what is S supposed to be too ?

# 	while start:
# 		r, c = start.pop()
# 		# visited.add((r,c))
		
# 		i += 1
# 		# if i >= 5: break # infinite loop control
		
# 		valid = 0

# 		if data[r][c] == "L" or data[r][c] == "S":
# 			if r-1 >= 0: # up
# 				if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
# 					start.append((r-1,c))
# 					valid += 1
# 			if c+1 < len(data[0]): # right
# 				if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
# 					start.append((r,c+1))
# 					valid += 1

# 		if data[r][c] == "J" or data[r][c] == "S":
# 			if r-1 >= 0: # up
# 				if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
# 					start.append((r-1,c))
# 					valid += 1
# 			if c-1 >= 0: # left
# 				if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
# 					start.append((r,c-1))
# 					valid += 1
		
# 		if data[r][c] == "7" or data[r][c] == "S":
# 			if c-1 >= 0: # left
# 				if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
# 					start.append((r,c-1))
# 					valid += 1
# 			if r+1 < len(data): # down
# 				if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
# 					start.append((r+1,c))
# 					valid += 1

# 		if data[r][c] == "F" or data[r][c] == "S":
# 			if c+1 < len(data[0]): # right
# 				if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
# 					start.append((r,c+1))
# 					valid += 1
# 			if r+1 < len(data): # down
# 				if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
# 					start.append((r+1,c))
# 					valid += 1

# 		if data[r][c] == "|" or data[r][c] == "S":
# 			if r-1 >= 0: # up
# 				if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
# 					start.append((r-1,c))
# 					valid += 1
# 			if r+1 < len(data): # down
# 				if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
# 					start.append((r+1,c))
# 					valid += 1

# 		if data[r][c] == "-" or data[r][c] == "S":
# 			if c-1 >= 0: # left
# 				if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
# 					start.append((r,c-1))
# 					valid += 1
# 			if c+1 < len(data[0]): # right
# 				if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
# 					start.append((r,c+1))
# 					valid += 1

# 		# there should be only 2 valid in each case

# 		print(valid, start)

# 	# print(start)


def part1(data):
	print(data)
	sr, sc = 0, 0
	for r in range(len(data)):
		for c in range(len(data[0])):
			if data[r][c]=="S":
				sr = r
				sc = c
				# print(f"found S at {r, c}")
				break
	start = deque([(sr, sc)])
	visited = set()
	visited.add((sr, sc))
	while start:
		r, c = start.pop()
		if data[r][c] == "L" or data[r][c] == "S":
			if r-1 >= 0: # up
				if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
					start.append((r-1,c))
					visited.add((r-1,c)) # I think I am a little confused
			if c+1 < len(data[0]): # right
				if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
					start.append((r,c+1))
					visited.add((r,c+1))

		if data[r][c] == "J" or data[r][c] == "S":
			if r-1 >= 0: # up
				if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
					start.append((r-1,c))
					visited.add((r-1,c))
			if c-1 >= 0: # left
				if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
					start.append((r,c-1))
					visited.add((r,c-1))
		
		if data[r][c] == "7" or data[r][c] == "S":
			if c-1 >= 0: # left
				if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
					start.append((r,c-1))
					visited.add((r,c-1))
			if r+1 < len(data): # down
				if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
					start.append((r+1,c))
					visited.add((r+1,c))

		if data[r][c] == "F" or data[r][c] == "S":
			if c+1 < len(data[0]): # right
				if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
					start.append((r,c+1))
					visited.add((r,c+1))
			if r+1 < len(data): # down
				if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
					start.append((r+1,c))
					visited.add((r+1,c))

		if data[r][c] == "|" or data[r][c] == "S":
			if r-1 >= 0: # up
				if (data[r-1][c] in "7F|" and (r-1,c) not in visited):
					start.append((r-1,c))
					visited.add((r-1,c))
			if r+1 < len(data): # down
				if (data[r+1][c] in "LJ|"  and (r+1,c) not in visited):
					start.append((r+1,c))
					visited.add((r+1,c))

		if data[r][c] == "-" or data[r][c] == "S":
			if c-1 >= 0: # left
				if (data[r][c-1] in "-LF"  and (r,c-1) not in visited):
					start.append((r,c-1))
					visited.add((r,c-1))
			if c+1 < len(data[0]): # right
				if (data[r][c+1] in "-J7"  and (r,c+1) not in visited):
					start.append((r,c+1))
					visited.add((r,c+1))

		# there should be only 2 valid in each case

		# print(start)
	print(visited)
	print(len(visited)//2) # it is not emmediately obvious to me why this is the correct answer

	# print(start)

part1(data)


