data = open('test.txt', 'r').read().split('\n')

from collections import deque
# my try: I am not very good at dfs, bfs problem
# I think my approach is dfs --> so its not correct; we care of min path so it has to be bfs
def part1(grid):
    [print(g) for g in grid]
    N = len(grid)
    M = len(grid[0])
    visited = set() # is this scope correct

    def is_valid(i,j,step): 
        if not (0 <= i < N and 0 <= j < M): return False
        if (i,j) in visited: return False
        if step == 0: return False
        return True

    ans = 0
    def dfs(r, c, d, step, total): # handle the step 
        # if moving in same direction reduce step;
        # if moving in different direction reset step
        # if step is 3 forced to change direction
        stack = deque([(r,c,d,step,total)])

        while stack:
            i, j, d, step, total = stack.popleft() # pop left from deque is more match
            if not is_valid(i, j, step): continue
            visited.add((i,j)) # does it need direction and step ?
            
            print(f'exploring i, j , {i, j}, {grid[i][j]}, {d}, {step} total : {total} ')
            curr = int(grid[i][j])
            
            if (i == N-1 and j == M-1):
              nonlocal ans
              ans = max(ans, total+curr)
              return

            step -= 1
            # same direction logic
            if d == "u":
                stack.append((i+1, j, d, 3, total+curr)) # down
                stack.append((i, j+1, d, 3, total+curr)) # right
                # can do this only if step valid
                if step:
                    stack.append((i-1, j, d, step, total+curr)) # up

            elif d == "d":
                stack.append((i, j+1, d, 3, total+curr)) # right
                stack.append((i-1, j, d, 3, total+curr)) # up
                # can do this only if step valid
                if step:
                    stack.append((i+1, j, d, step, total+curr)) # down

            elif d == "r":
                stack.append((i+1, j, d, 3, total+curr)) # down
                stack.append((i-1, j, d, 3, total+curr)) # up
                # can do this only if step valid
                if step:
                    stack.append((i, j+1, d, step, total+curr)) # right

            if step == 0: step = 3 # reset step
    
    dfs(0, 0, 'r', 3, 0)
    print('ans is ', ans)
    return ans            

    # ans = 0
    # stack = [(0, 0)] # is this scope correct
    # def explore(i, j, step, total):
    #     if not in_bounds(i,j): return
    #     if (i,j) in visited: return

    #     if i == N-1 and j == M-1: # we reach the end
    #         nonlocal ans
    #         ans = max(ans, total)
    #         return

    #     if step == 0: step = 3 
    #     visited.add((i,j))
    #     # can explore 3 directions as long as step is not 3
    #     new_total = total + int(grid[i][j]) # we need to ignore the first one
    #     explore(i+1,j,step-1, new_total) # down
    #     explore(i-1,j,step-1, new_total) # up
    #     explore(i,j+1,step-1, new_total) # right
    #     # while stack:
    #     #     x,y = stack.pop()
    #     return

    # explore(0, 0, 3, 0)




# NOTE : I couldn't do even part1; diajktra's with conditions
# but I will do it before aoc23 ends
part1(data)
