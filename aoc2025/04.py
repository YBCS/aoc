data = open("inp.txt", "r").read().split("\n")
data = [list(d) for d in data]
dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]  # up right down left top-left top-right bottom-left bottom-right
ROWS = len(data)
COLS = len(data[0])


def part1(data):
    locs = []
    ans = 0
    for r in range(ROWS):
        for c in range(COLS):
            if data[r][c] == "@":
                count = 0
                for di, dj in dirs:
                    i, j = r + di, c + dj
                    if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                        continue
                    if data[i][j] == "@":
                        count += 1

                if count < 4:
                    locs.append((r, c))
                    ans += 1

    print(ans)
    return ans, locs


def part2(data):
    ans = 0
    while True:
        counts, outs = part1(data)
        for i, j in outs:
            data[i][j] = "."
        ans += counts
        if not outs:
            break
    print(ans)


part2(data)
