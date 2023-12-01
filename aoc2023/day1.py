data = open('input.txt', 'r').read().split('\n')

def part1(data):
	nums = "123456789"
	ans = 0
	for word in data:
		l = 0
		r = len(word)-1
		print('cur word ', word)
		while word[l] not in nums:
			l += 1
		while word[r] not in nums:
			r -= 1

		num = int(word[l]+word[r])
		ans += num
	return ans

def part2(data):
	ans = 0
	word_nums = [
		"one", "two", "three", 
		"four", "five", "six", 
		"seven", "eight", "nine", 
		"1", "2", "3", 
		"4", "5", "6", 
		"7", "8", "9"
	]
	nums = "123456789"
	# only use word_map ?
	word_map = {
	"one" : "1",
	"two" : "2",
	"three" : "3",
	"four" : "4",
	"five" : "5",
	"six" : "6",
	"seven" : "7",
	"eight" : "8",
	"nine" : "9",
	}

	# 7pqrstsixteen
	for word in data:

		l = 100 # some big no.
		r = -1

		first = -1
		second = -1
		for n in word_nums:
			temp1 = word.find(n)
			temp2 = word.rfind(n)
			if temp1 != -1:
				if temp1 < l:
					l = temp1
					first = n
				if temp2 != -1 and temp2 > r:
					r = temp2
					second = n
				# l = min(l, temp)
				# r = max(r, temp)
		# print(f"found l {l} and r {r} {first, second}")
		
		num = ""
		if first in nums:
			num += first
		else:
			num += word_map[first]
		
		if second in nums:
			num += second
		else:
			num += word_map[second]
		ans += int(num)

		# print(f'final ans is {ans} and input was {word}')
	print('ans is ', ans)



# def part2(data):
# 	ans = 0
# 	nums = "123456789"
# 	word_map = {
# 	"one" : "1",
# 	"two" : "2",
# 	"three" : "3",
# 	"four" : "4",
# 	"five" : "5",
# 	"six" : "6",
# 	"seven" : "7",
# 	"eight" : "8",
# 	"nine" : "9",
# 	}

# 	for word in data:
# 		l = 100 # some big no.
# 		r = -1
# 		first = -1
# 		second = -1

# 		for k, v in word_map.items():
# 			for i in [k,v]:
# 				temp = word.find(i)
# 				if temp != -1:
# 					if temp < l:
# 						l = temp
# 						first = n
# 					if temp > r:
# 						r = temp
# 						second = n

# 		print(f"found l {l} and r {r} {first, second}")
		
# 		num = ""
# 		if first in nums:
# 			num += first
# 		else:
# 			num += word_map[first]
		
# 		if second in nums:
# 			num += second
# 		else:
# 			num += word_map[second]
# 		ans += int(num)

# 		print(f'final ans is {ans}')

print(part2(data))
