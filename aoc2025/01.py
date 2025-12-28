# advent of code day 1

data = open("inp.txt", "r").read().split("\n")

# """ part 1 🌟

point = 50
count = 0
for rot in data:
    side, num = rot[0], int(rot[1:])
    if side == "L":
        point = (point - num) % 100  # I dont understand how modulo works
        if point < 0:
            point = 100 + point
    else:
        point = (point + num) % 100
        if point > 99:
            point = point - 100
    if point == 0:
        count += 1

print(count)
# """

""" # part 2
# this solution so funny 😭 thanks john
point = 50
count = 0
for rot in data:
    side, num = rot[0], int(rot[1:])
    operator = -1 if side == "L" else 1
    for _ in range(num):
        point += operator
        if side == "L" and point == -1:
            point = 99
        elif side == "R" and point == 100:
            point = 0
        if point == 0:
            count += 1
print(count)
"""
