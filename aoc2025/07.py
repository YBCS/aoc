from collections import deque
from functools import cache

items = open("inp.txt", "r").read().split("\n")
items = [list(item) for item in items]


def part2(items):
    ROWS = len(items)
    COLS = len(items[0])

    start = None
    for i in range(COLS):
        if items[0][i] == "S":
            start = i

    # count = 0

    # def dfs(r, c):
    #     nonlocal count
    #     if r > ROWS or c >= COLS or c < 0:
    #         return
    #     if r == ROWS:
    #         # there is a very strong assumption here
    #         count += 1
    #         return

    #     if items[r][c] == ".":
    #         dfs(r + 1, c)
    #     else:
    #         dfs(r + 1, c + 1)
    #         dfs(r + 1, c - 1)

    # happy with this one
    @cache
    def dfs(r, c):
        if r > ROWS or c >= COLS or c < 0:
            return 0
        if r == ROWS:
            return 1

        if items[r][c] == ".":
            return dfs(r + 1, c)
        else:
            a = dfs(r + 1, c + 1)
            b = dfs(r + 1, c - 1)
            return a + b

    out = dfs(0, start)
    print(out)


part2(items)


def part1(items):
    ROWS = len(items)
    COLS = len(items[0])

    start = None
    for i in range(COLS):
        if items[0][i] == "S":
            start = i
            break

    assert start is not None

    stack = deque([(0, start)])
    SEEN = set()
    ans = 0
    while stack:
        r, c = stack.popleft()
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        if r + 1 < ROWS:
            if items[r + 1][c] == ".":
                stack.append((r + 1, c))
            elif items[r + 1][c] == "^":
                ans += 1
                if c + 1 < COLS:
                    stack.append((r + 1, c + 1))
                if c - 1 >= 0:
                    stack.append((r + 1, c - 1))
            else:
                print("invalid option")

    print(ans)


# part1(items)
