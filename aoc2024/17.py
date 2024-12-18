from collections import defaultdict, deque
import re

def combo(operand, a, b, c):
	if 0 <= operand <= 3: return operand
	if operand == 4: return a
	if operand == 5: return b
	if operand == 6: return c
	print("error combo")
	return

def part1(data):
	# referenced hyperneutrino

	a,b,c, *program = map(int, re.findall(r"\d+", data))
	print(a,b,c, program)
	
	output = []
	i = 0
	while i < len(program):
		opcode = program[i]
		operand = program[i+1]

		if opcode == 0: 	# adv
			a = a >> combo(operand, a,b,c)
		elif opcode == 1:	# bxl
			b = b ^ operand
		elif opcode == 2:	# bst
			b = combo(operand, a,b,c) % 8
		elif opcode == 3:	# jnz
			if a != 0:
				i = operand
				continue
		elif opcode == 4:	# bxc
			b = b ^ c	
		elif opcode == 5:	# out
			output.append(combo(operand, a,b,c) % 8)
		elif opcode == 6:	# bdv
			b = a >> combo(operand, a,b,c)			
		elif opcode == 7:	# cdv
			c = a >> combo(operand, a,b,c)			
		i += 2

	print(*output, sep=",")

def part2(): 
	pass

if __name__ == "__main__":	
	file = "in.txt"
	file = "eg.txt"
	data = open(file, "r").read()


	part1(data)
	part2()




