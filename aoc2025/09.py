from collections import defaultdict

items = open("inp.txt", "r").read().split("\n")
red_tiles = []
for item in items:
    r, c = map(int, item.split(","))
    red_tiles.append((c, r))
"""
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............



..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
"""


def find_area(pair_1, pair_2):
    # check if all four corner in valid region;
    x1, y1 = pair_1
    x2, y2 = pair_2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def valid(pair_1, pair_2):
    # implementing this will make me a men 😭
    return True


def part2(red_tiles):
    print("part 2 ")
    # actually create the grid
    row_map = defaultdict(set)
    col_map = defaultdict(set)

    for r, c in red_tiles:
        row_map[r].add(c)
        col_map[c].add(r)
    pairs_ab = set(red_tiles)

    print(sorted(pairs_ab))
    # print("pairs_ab ", pairs_ab)
    # print("row_map ", row_map)
    # print("col_map ", col_map)

    st_r, st_c = sorted(red_tiles)[0]
    # print("st_r, st_c ", st_r, st_c)

    # ..............
    # .......#XXX#..
    # .......XXXXX..
    # ..#XXXX#XXXX..
    # ..XXXXXXXXXX..
    # ..#XXXXXX#XX..
    # .........XXX..
    # .........#X#..
    # ..............
    boundary_coordinates = []
    cr, cc = st_r, st_c
    nr, nc = None, None
    # pairs_ab.remove((st_r, st_c))
    row_map[st_r].remove(st_c)
    col_map[st_c].remove(st_r)
    prev = None
    while True:
        if nr == st_r and nc == st_c:
            break
        print("cr, cc ", cr, cc)
        nr, nc = None, None
        # traverse clockwise and store all boundary coordinates
        # frmo cr, cc try all 4 directions and assign nr and nc
        # all points in between goes to boundary
        cols = row_map[cr]
        rows = col_map[cc]

        # what about the prev avoidance stuff
        for col in cols:
            if (cr, col) in pairs_ab:  # not yet used
                if col > cc:  # found in right
                    # mark used
                    pairs_ab.remove((cr, col))
                    row_map[cr].remove(col)  # we dont need prev ?
                    nr, nc = cr, col
                    prev = "right"
                    for c in range(cc, col + 1):
                        boundary_coordinates.append((cr, c))
                    break

        for row in rows:
            if (row, cc) in pairs_ab:
                if row > cr:  # found in down
                    pairs_ab.remove((row, cc))
                    col_map[cc].remove(row)
                    nr, nc = row, cc
                    prev = "down"
                    for r in range(cr, row + 1):
                        boundary_coordinates.append((r, cc))
                    break

        for col in cols:  # try left and right
            if (cr, col) in pairs_ab:  # not yet used
                if col < cc:  # found in left
                    # remove from the pairs ab (marking as used)
                    pairs_ab.remove((cr, col))
                    row_map[cr].remove(col)
                    nr, nc = cr, col
                    prev = "left"
                    for c in range(col, cc + 1):
                        boundary_coordinates.append((cr, c))
                    break

        for row in rows:
            if (row, cc) in pairs_ab:
                if row < cr:  # found in up
                    # remove from the pairs ab
                    pairs_ab.remove((row, cc))
                    col_map[cc].remove(row)
                    nr, nc = row, cc
                    prev = "up"
                    for r in range(row, cr + 1):
                        boundary_coordinates.append((r, cc))
                    break

        print("reach here ", nr, nc, st_r, st_c)
        cr, cc = nr, nc

    print("boundary_coordinates ", boundary_coordinates)


part2(red_tiles)


def part1(red_tiles):
    # pairs_ab = sorted(red_tiles, key=lambda x: x[1])
    pairs_ab = sorted(red_tiles)

    print(pairs_ab)
    size = len(pairs_ab)
    ans = 0
    for i in range(size):
        for j in range(i + 1, size):
            area = find_area(pairs_ab[i], pairs_ab[j])
            ans = max(ans, area)

    print(ans)


# part1(red_tiles)
