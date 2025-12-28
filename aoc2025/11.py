from collections import defaultdict, deque
from functools import cache

items = open("inp.txt", "r").read().split("\n")


def part2(items):
    graph = defaultdict(list)

    for item in items:
        key, *conn = item.split(" ")
        # print(key, conn)
        graph[key[:-1]].extend(conn)

    start = "svr"
    end = "out"

    ans = 0

    @cache
    def dfs(curr, fft_var, dac_var):
        if curr == "fft":
            fft_var = True
        if curr == "dac":
            dac_var = True
        if curr == end:
            return 1 if fft_var and dac_var else 0
        ans = 0
        for neigh in graph[curr]:
            ans += dfs(neigh, fft_var, dac_var)
        return ans

    ans = dfs(start, False, False)
    print(ans)


part2(items)


def part2_(items):
    # iterative and no pruning; not good enough
    graph = defaultdict(list)

    for item in items:
        key, *conn = item.split(" ")
        graph[key[:-1]].extend(conn)

    start = "svr"
    end = "out"

    ans = 0
    stack = deque([(start, False, False)])
    while stack:
        # print("len ", len(stack))
        curr, fft_var, dac_var = stack.popleft()

        if curr == "fft":
            fft_var = True
        if curr == "dac":
            dac_var = True

        if curr == "out" and fft_var and dac_var:
            ans += 1
        for neigh in graph[curr]:
            stack.append((neigh, fft_var, dac_var))

    print(ans)


def part1(items):
    graph = defaultdict(list)

    for item in items:
        key, *conn = item.split(" ")
        # print(key, conn)
        graph[key[:-1]].extend(conn)

    start = "you"
    end = "out"

    ans = 0
    stack = deque([start])
    while stack:
        curr = stack.popleft()
        if curr == "out":
            ans += 1
        for neigh in graph[curr]:
            stack.append(neigh)

    print(ans)
