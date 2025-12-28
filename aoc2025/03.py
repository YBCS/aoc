data = open("inp.txt", "r").read().split("\n")
data = "987654321111111,811111111111119,234234234234278,818181911112111"

""" part 1
98
89
78
92


find largest
find largest in left 
find largest in right 
compare the two numbers formed

99999999

def get_largest_index(arr):
    if not arr:
        return
    largest = max(arr)
    largest_i = arr.index(largest)
    return largest, largest_i


# data = data.split(",")
# no one has written more litteral code 🤨😭
ans = 0
for d in data:
    nums = list(map(int, list(d)))
    big, big_i = get_largest_index(nums)
    left = nums[:big_i]
    right = nums[big_i + 1 :]

    big_cache = big
    if left:
        left_big, _ = get_largest_index(left)
        big = int(str(left_big) + str(big))
    if right:
        right_big, _ = get_largest_index(right)
        big = max(int(str(big_cache) + str(right_big)), big)
    print(big)
    ans += big
print("ans ", ans)

"""


""" part 2
DP ahh question 🧨🤨😭
234234234234278
try all nums of len 12 and get the biggest out; 
"""


def get_largest_12dgt(d, i, used):
    # d is (whole) digit in string (has at least 12 digits)
    # i is index of where in d we are currently processing
    # used is how much of 12 digit we are generating is generated so far

    if i == 11 and used == 12:
        return d[i]

    if i > 11:
        return ""

    if used > 12:
        return ""

    big = d[i] + get_largest_12dgt(d, i, used)  # use i
    get_largest_12dgt(d, i, used)  # dont use i

    return big


data = data.split(",")
ans = 0
for d in data:
    size = len(d)
    for i in range(size - 12):
        big = get_largest_12dgt(d[i:], 0, 0)
    print(big)
    ans += big
print("ans ", ans)
