from collections import defaultdict

data = open('input.txt', 'r').read().split('\n')

def part1(data):
	# print(data)
	ans = 0
	for row in range(len(data)):
		num = ""
		symbol_found = False
		for col in range(len(data[0])):
			# check all 8 neighbours
			if data[row][col].isdigit() :
				num += data[row][col]
				neighbours = [(-1,-1),(-1,0),(-1,1),
				 			  (0,-1),(0,1),
				 			  (1,-1),(1,0),(1,1)]
				for i, j in neighbours:
					if row+i >= 0 and row+i < len(data) and col+j < len(data[0]) and col+j >=0: # in bounds
						cur_neighbour =  data[row+i][col+j]
						if cur_neighbour != "." and not cur_neighbour.isdigit(): # symbol found
							symbol_found = True
							break
			else:
				if num:
					if symbol_found:
						ans += int(num)
						symbol_found = False
					num = ""
			
			# okay the bug is those numbers who are in the edge # is there a better way to handle this
			if col == len(data[0])-1:
				if num:
					if symbol_found:
						ans += int(num)
	print(f'ans is {ans}')


# 607896 too high 
# 544359 low ? 
# 546563

def part2(data):
	ans = 0
	symbol_pos = defaultdict(list)
	'''
	when a symbol is found; keep track of all of its neighbouring nums
	'''
	for row in range(len(data)):
		num = ""
		symbol_found = False
		cur_symbol_key = ""
		for col in range(len(data[0])):
			if data[row][col].isdigit() :
				num += data[row][col]
				neighbours = [(-1,-1),(-1,0),(-1,1),
				 			  (0,-1),(0,1),
				 			  (1,-1),(1,0),(1,1)]
				for i, j in neighbours:
					if row+i >= 0 and row+i < len(data) and col+j < len(data[0]) and col+j >=0: # in bounds
						cur_neighbour =  data[row+i][col+j]
						if cur_neighbour != "." and not cur_neighbour.isdigit(): # symbol found
							symbol_found = True
							cur_symbol_key = f'{row+i}, {col+j}'
							break
			else:
				if num:
					if symbol_found and cur_symbol_key:
						symbol_pos[cur_symbol_key].append(num)
						cur_symbol_key = ""
						symbol_found = False
					num = ""

			# okay the bug is those numbers who are in the edge # is there a better way to handle this
			if col == len(data[0])-1:
				if num:
					if symbol_found and cur_symbol_key:
						symbol_pos[cur_symbol_key].append(num)
	
	for vals in symbol_pos.values():
		if len(vals) == 2:
			ans += (int(vals[0]) * int(vals[1]))

	# print(symbol_pos)
	print(f'final ans is {ans}')


# 15270285566094374 too high
# 91031374 

part2(data)
