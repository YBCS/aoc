# day 21 

from collections import deque
data = open('input.txt', 'r').read().split('\n')


def part1(data):
    sr, sc = (0,0)
    # actually start is smack in middle so (n//2,n//2); n = len(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                start = (i,j) # for test -> (5,5)
                break
    
    visited = set()
    queue = deque([(sr,sc,0)])
    ans = set()  ## I dont get the point of this stuff

    def is_valid(i,j):
        return 0 <= i < len(data) and 0 <= j < len(data[0]) and (i,j) not in visited and data[i][j] != "#"

    while queue:
        r, c, d = queue.popleft()
        if not is_valid(r, c): continue  # checking here prevents duplicate work ?
        visited.add((r,c))
        if d <= 64 and d%2 == 0:  # why do we modulo two here ?
            ans.add((r,c))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        for i, j in dirs:
                queue.append((r+i, c+j, d+1))

    print(len(ans))


# part1(data)
part1Sol(data)