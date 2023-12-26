# # day 23 
# from collections import deque
# adapted from https://github.com/ypisetsky/advent-of-code-2023/blob/main/day23.py

import sys

data = open('input.txt', 'r').read().split('\n')

# lol :P 😛
sys.setrecursionlimit(1000000)

# my own
def part1(data):
    # [print(d) for d in data]

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = set([(0,1)])

    def is_valid(r, c):
        return 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] != "#" and (r,c) not in visited

    def dfs(r,c):
        neighbours = []

        if r == len(data)-1 and c == len(data[0])-2:
            print('reach destination with steps : ', len(visited)-1)
            return len(visited)-1
        
        cur = data[r][c]
        if cur == '.':
            neighbours = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        if cur in '><^v':
            if cur == ">":
                neighbours = [(r, c+1)]
            elif cur == "<":           
                neighbours = [(r, c-1)]
            elif cur == "^":                
                neighbours = [(r-1, c)]
            elif cur == "v":                
                neighbours = [(r+1, c)]
        
        ans = -float('inf')
        for nr,nc in neighbours:
            if not is_valid(nr, nc): continue
            visited.add((nr,nc))
            ans = max(ans, dfs(nr, nc))
            visited.remove((nr,nc))
        return ans
    
    return dfs(0,1)

# my own
def part2(data):
    visited = set([(0,1)])

    def is_valid(r, c):
        return 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] != "#" and (r,c) not in visited

    def dfs(r,c):
        neighbours = []

        if r == len(data)-1 and c == len(data[0])-2:
            print('reach destination with steps : ', len(visited)-1)
            return len(visited)-1
        
        neighbours = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        ans = -float('inf')
        for nr,nc in neighbours:
            if not is_valid(nr, nc): continue
            visited.add((nr,nc))
            ans = max(ans, dfs(nr, nc))
            visited.remove((nr,nc))
        return ans
    
    return dfs(0,1)

# adapted from github.com/ypisetsky
def part1_ypisetsky(data):

    seen = set([(0,1)])
    def dfs(i,j):
        neighbours = None
        
        if i == len(data)-1 and j == len(data[0])-2:
            print('path length is ', len(seen)-1)
            return len(seen)-1
        
        if data[i][j] == '.': # where did this 'X' come from
            neighbours = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        elif data[i][j] == '>':
            neighbours = [(i, j + 1)]
        elif data[i][j] == '<':
            neighbours = [(i, j - 1)]            
        elif data[i][j] == 'v':
            neighbours = [(i + 1, j)]
        elif data[i][j] == '^':
            neighbours = [(i - 1, j)]

        best = None
        for neighbor in neighbours:
            (x, y) = neighbor
            if neighbor in seen or data[x][y] == "#":
                continue
            seen.add(neighbor)
            res = dfs(x, y)
            if best is None or (res is not None and res > best):
                best = res
            seen.remove(neighbor)
        return best

    return dfs(0,1)

def part2_ypisetsky(data):

    seen = set([(0,1)])

    def dfs(i,j):
        neighbours = None
        
        if i == len(data)-1 and j == len(data[0])-2:
            # print('path length is ', len(seen)-1)
            return len(seen)-1
        
        neighbours = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

        best = None
        for neighbor in neighbours:
            (x, y) = neighbor
            if neighbor in seen or data[x][y] == "#":
                continue
            seen.add(neighbor)
            res = dfs(x, y)
            if best is None or (res is not None and res > best):
                best = res
            seen.remove(neighbor)
        return best

    return dfs(0,1)

# print('final output is ', part1(data))
print('final output is ', part2(data))
# print('final output is ', first_attempt(data))


