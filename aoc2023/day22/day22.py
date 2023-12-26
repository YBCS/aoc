# day 22

# INCOMPLETE 

data = open('test.txt', 'r').read().split('\n')

def part1(data):
    names = 'abcdefg'
    max_x, max_y, max_z = 0,0,0
    for coor in data:
        left, right = coor.split('~')
        left = list(map(int, left.split(',')))
        right = list(map(int, right.split(',')))

        print(left, right)
        for i in range(len(left)):
            max_x = max(max_x, left[0], right[0])
            max_y = max(max_x, left[1], right[1])
            max_z = max(max_x, left[2], right[2])

    # max_x = 2 max_z = 9
    xz_grid = [list('.'*(max_x+1)) for _ in range(max_z+1)]
    yz_grid = [list('.'*(max_y+1)) for _ in range(max_z+1)]
    print(xz_grid)
    print(yz_grid)

    for i, coor in enumerate(data):
        left, right = coor.split('~')
        left = list(map(int, left.split(',')))
        right = list(map(int, right.split(',')))
        
        # fill xz 
        lx, lz = left[0], left[-1]
        rx, rz = right[0], right[-1]
        direction = ""
        if lx == rx: direction = "up" # my assumption at the moment is that it can only fill up or left (probably wrong)
        if lz == rz: direction = "left" # the example has so far not shown any eg where it fills both row and col
        
        if direction == "up":
            for d in range(lz, rz+1):
                xz_grid[lx][d] = i
        if direction == "left":
            for d in range(lx, rx+1):
                xz_grid[lz][d] = i

    [print(g) for g in xz_grid]
    # make grid
    # compression; or simulate making it fall down
    # count without support




part1(data)