
data = open('input.txt', 'r').read().split('\n')

# def part1(data):
# 	seeds = list(map(int, data[0].split(':')[1].strip().split(' ')))
# 	data = data[2:]
# 	# print('data ', data)
# 	print(seeds)
# 	ans = float("inf")
# 	cur_map = {}
# 	for cur_seed in seeds:
# 		mapping = cur_seed
# 		for i, info in enumerate(data):
# 			if info:
# 				# print(info)
# 				if info[0].isdigit():
# 					destination, source, span = map(int, info.split(' '))
# 					# print(destination, source, span)
# 					for i in range(span): # I am sure this can be avoided; oh no this has to be avoided 💀
# 						cur_map[source+i] = destination+i
# 				# else:
# 					# print(info) # label
# 			else:
# 				# processing
# 				# print(cur_map) # I am having to add an empyt new line in the input just for this to work 😵
# 				if mapping in cur_map:
# 					mapping = cur_map[mapping] # verify
# 				# else:
# 				# 	mapping = cur_seed
# 				# cur_seed = mapping
# 				cur_map = {}

# 		print('mapped to ', mapping)
# 		ans = min(ans, mapping)

# 	print(f'ans is {ans}')

def part1(data):
	seeds = list(map(int, data[0].split(':')[1].strip().split(' '))) # take one input for now 
	data = data[2:]
	print('data ', data)
	print('seeds ', seeds)
	ans = float("inf")
	cur_map = {}
	for cur_seed in seeds:
		mapping = cur_seed
		for i, info in enumerate(data):
			if info:
				if info[0].isdigit():
					destination, source, span = map(int, info.split(' '))
					delta = destination - source
					cur_map[i] = (destination, source, span, delta) # I dont need the destination
			else:
				for destination, source, span, delta in cur_map.values():
					# print(f'checking for {mapping} in between {source} and {source+span-1}')
					if source <= mapping <= source+span-1:
						mapping = mapping + delta
						# print('found mapping ', mapping)
						# print()
						break
					print(destination,source,span,delta)
				print()
				cur_map = {}


		ans = min(ans, mapping)

	print(f'ans is {ans}')


def part2(data):
	seeds = list(map(int, data[0].split(':')[1].strip().split(' ')))
	data = data[2:]
	
	ans = float("inf")
	for i in range(0, len(seeds), 2):
		a, b = seeds[i], seeds[i+1]
		seed_range = [i for i in range(a, a+b)] # this is insane 😭

		cur_map = {}
		for cur_seed in seed_range:
			mapping = cur_seed
			for i, info in enumerate(data):
				if info:
					if info[0].isdigit():
						destination, source, span = map(int, info.split(' '))
						delta = destination - source
						cur_map[i] = (destination, source, span, delta) # I dont need the destination
				else:
					for destination, source, span, delta in cur_map.values():
						if source <= mapping <= source+span-1:
							mapping = mapping + delta
							break
						# print(destination,source,span,delta)
					# print()
					cur_map = {}
			ans = min(ans, mapping)
	print('ans is ', ans)
	return



part2(data)
