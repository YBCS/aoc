data = open('input.txt', 'r').read().split('\n')[0].split(',')

def calcHash(chars):
	ans = 0
	for c in chars:
		ans += ord(c)
		ans *= 17
		ans = ans % 256
	return ans

def part1(data):
	temp = list(map(calcHash, data))
	return sum(temp)

def part2(data):
	boxes = {i: [] for i in range(256)}
	for letters in data:
		print(letters)
		if "-" in letters:
			label = letters.split("-")[0]
			operation = "-"
		elif "=" in letters:
			label, focal = letters.split("=")
			operation = "="

		# label, operation, focal = letters[:2], letters[2:3], letters[3:] # this was the bug; letter can be longer than just 4 chars
		box = calcHash(label)
		box_labels = [l for l, f in boxes[box]]
		if operation == "-":
			if label in box_labels:
				i = box_labels.index(label)
				boxes[box] = boxes[box][:i] + boxes[box][i+1:]
		if operation == "=":
			to_store = (label, focal)
			if label in box_labels:
				i = box_labels.index(label)
				boxes[box][i] = to_store
			else:
				boxes[box].append(to_store)
	# [print(b, ite) for b, ite in boxes.items() if ite]
	ans = 0
	for box in range(256):
		for index, (slot,focal) in enumerate(boxes[box]):
			ans += (box+1) * (index+1) * int(focal) 
	return ans



# calcHash('pc')
print(part2(data)) # 52301 too low ?



# split letters into label and operation and focal
# get hash of label to find box
# if operation -
  # go to box and remove label if it exist # this might bot be as straightforward
# if operation =
  # go to box and store [label focal]
	# if label already exist; update focal
	# else store in end of box

# do I need a linked list ?? 
# maybe ? or I can optionally reconstruct the list everytime; atmost 256 operations
