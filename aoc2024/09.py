from collections import defaultdict, deque


def count_block(block):
	ans = 0
	for i, num in enumerate(block):
		if num == ".":
			break
		ans += num * i
	return ans

def part1(block):
	# now swapping stuff until they are no . in between
	i = 0
	j = len(block) - 1
	while block[i] != ".":
		i += 1
	while block[j] == ".":
		j -= 1
	
	while i <= j:
		if block[i] != "." and block[j] ==".":
			i += 1
			j -= 1
			continue
		if block[i] != ".":
			i += 1
			continue
		elif block[j] == ".":
			j -= 1
			continue

		block[i], block[j] = block[j], block[i]
		i += 1
		j -= 1

	# i is at first '.' after fix
	# print('block fixed ', block, i, j, block[i], block[j])

	ans = count_block(block)
	print(ans)

def part2(block):
	print('part 2 block ', block)
	i = 0
	block_dict = {}
	while i < len(block):
		cur_id = block[i]
		cur_count = 0
		while i < len(block) and block[i] != "." and block[i] == cur_id:
			i += 1
			cur_count += 1
		cur_space = 0
		while i < len(block) and block[i] == ".":
			cur_space += 1
			i += 1

		block_dict[cur_id] = ((cur_count, cur_space))
	
	# print(block)
	print(block_dict)
	while cur_id >= 0:
		count, space = block_dict[cur_id]
		for pre_id in range(cur_id):
			pre_count, pre_space = block_dict[pre_id]
			diff = pre_space - count
			# if count <= pre_space:
				# pre_space -= count
			if diff >= 0:
				print('updated')
				block_dict[pre_id] = (pre_count, 0)
				if cur_id - 1 >= 0:
					p_count, p_space = block_dict[cur_id-1]
					block_dict[cur_id-1] = (p_count, p_space + count + space)
					block_dict[cur_id] = (count, diff)
				break
		print(cur_id, block_dict)
		cur_id -= 1
	# print(block_dict)

# working
def part2II(block):
	# print('the block ', block, len(block))
	# store id size; pos
	# store space size; pos
	block_dict = {}
	spaces = []
	_id = 0
	i = 0
	while i < len(block):
		if block[i] != ".": # parsing id
			start = i
			size = 0
			while i < len(block) and block[i] != "." and block[i] == block[start]:
				size += 1
				i += 1
			block_dict[_id] = (start, size)
			_id += 1
			continue
		if block[i] == ".": # parsing space
			start = i
			size = 0
			while i < len(block) and block[i] == ".":
				size += 1
				i += 1
			spaces.append((start, size))
			continue

	# print(block_dict)
	# print(spaces)
	# print(_id)

	while _id > 0:
		_id -= 1
		start, size = block_dict[_id]
		for i, space in enumerate(spaces):
			space_start, space_size = space
			if space_start > start:
				break
			if space_size >= size:
				# update the block
				new_start = space_start
				block_dict[_id] = (new_start, size)
				# update the spaces --> do I need this info
				new_start = space_start + size
				new_size = space_size - size # it could become zero; all space was used
				spaces[i] = (new_start, new_size)
				break


		# if size
	# print('updated ')
	# print(block_dict)
	# print(spaces)
	ans = 0
	for key, val in block_dict.items():
		start, size = val
		# print(key, start, size)
		for i in range(size):
			ans += key * (start + i)
	print(ans)

if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	data = open(file, "r").read().split("\n")[0]

	block = []
	_id = 0
	for i in range(0, len(data)-1, 2):
		a, b = data[i], data[i+1]
		block.extend([_id] * int(a))
		block.extend(["."] * int(b))
		_id += 1
	block.extend([_id]*int(data[-1]))

	# part1(block)
	part2II(block)




