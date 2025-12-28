import re

items = open("inp.txt", "r").read().split("\n")

op = items.pop()
op = re.findall(r"[+*]", op)


"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def part_2(items, op):
    ROWS = len(items)
    COLS = len(op)

    # best compare with the i+1th item
    # please redo
    l = 0
    while l < len(items[0]):
        r = l
        while r < len(items[0]) and items[0][r] != " ":  # if its num
            r += 1

        curr_l, curr_r = l, r
        best_l, best_r = l, r
        print("l and r ", l, r)
        for i in range(l, r):
            # try going all the way to the bottom;
            # in each row try to expand both left and right to see the actual bounds
            for row in range(1, ROWS):
                left_moved = False
                while curr_l > 0 and items[row][curr_l] != " ":
                    left_moved = True
                    curr_l -= 1
                right_moved = False
                while curr_r < len(items[0]) and items[row][curr_r] != " ":
                    right_moved = True
                    curr_r += 1

                if left_moved:
                    curr_l += 1
                if right_moved:
                    curr_r -= 1

                best_l, best_r = min(best_l, curr_l), max(best_r, curr_r)
        print("best_l and best_r", best_l, best_r)

        # move l until u cross all num and then the next spaces ; until u find next set of nums
        l = len(items[0])


part_2(items, op)


def part_1(items, op):
    nums = []
    for num in items:
        out = list(map(int, re.findall(r"\d+", num)))
        nums.append(out)
    # print(nums)

    ROWS = len(nums)
    COLS = len(nums[0])
    ans = 0
    for c in range(COLS):
        curr_op = op[c]
        col = 0

        if curr_op == "*":
            col = 1
            for r in range(ROWS):
                col *= nums[r][c]

        if curr_op == "+":
            col = 0
            for r in range(ROWS):
                col += nums[r][c]

        ans += col

    print(ans)
