# day 18

'''
from input contruct grid

get max dimensions
reduce by those area which are outside of main loop 


how to :
    - get dimensionns of the grid -- idk this
    - calculate the area out of bounds
        - this is doable


HyperNeutrino has solved this very intuitively
https://github.com/hyper-neutrino/advent-of-code/blob/main/2023

get the edge points of the grid;
use points to calculate area using shoelace algorithm
fix offset using pick's theorem
'''

data = open('input.txt', 'r').read().split('\n')

# # simulation based attempt which will not work
# def part1(data):
#     print('data is ', data)
#     ROW, COL = 20, 20 # choose something arbitrary large; coz I don't know how to get the dimensions
#     # ROW, COL = 10,10 # choose something arbitrary large; coz I don't know how to get the dimensions
#     grid = [list('.'*COL) for _ in range(ROW)] # took me way too long to get this
#     # print("grid is ", grid)
#     start = (0,0)
#     r, c = start
#     grid[r][c] = "#"
#     for d in data:
#         di, n, color = d.strip().split(' ')
#         n = int(n)
#         for i in range(n):
#             if di == "L":
#                 c -= 1
#             elif di == "R":
#                 c += 1
#             elif di == "U":
#                 r  -= 1
#             elif di == "D":
#                 r += 1
#             grid[r][c] = "#"
#     [print(g) for g in grid]

def pickTheroem(shoelaceArea, b):
    # our use case is 
    # use area from shoelaceAlgorithm to find i; i is number of enclosed points # basically our area is i + b;
    # a = i + (b//2) - 1
    # i = a - (b//2) + 1
    enclosedPoints = shoelaceArea - (b//2) + 1
    return enclosedPoints

def shoelaceAlgorithm(points):
    # shoelace finds area enclosed so it should be less than required
    # also the area is from the middle of the each box; so there is offset to be fixed
    area = 0
    for i in range(1, len(points)-1):
        area += points[i][0] * (points[i-1][1] - points[i+1][1])
    return area // 2


def part1(data):
    print(data)
    points = [(0,0)]
    r,c = (0,0)
    b = 0 # boundary
    for item in data:
        di, n, color = item.split(' ')
        n = int(n)
        b += n
        if di == "R":
            c += n
        elif di == "L":
            c -= n
        elif di == "U":
            r -= n
        elif di == "D":
            r += n
        points.append((r,c))
    area = shoelaceAlgorithm(points) # still not sure how shoelaceAlgo and pickTherem is interacting so well
    area1 = pickTheroem(area, b)
    print(points)
    print(area)
    print(area1+b)


def decode(color):
    table = {0: "R", 1: "D", 2: "L", 3: "U"}
    di = int(color[-1])
    color = color[1:-1]
    return int(color, 16), table[di]


def part2(data):
    points = [(0,0)]
    r,c = (0,0)
    b = 0 # boundary
    for item in data:
        _, _, color = item.split(' ')
        n, di = decode(color[1:-1])
        b += n
        if di == "R":
            c += n
        elif di == "L":
            c -= n
        elif di == "U":
            r -= n
        elif di == "D":
            r += n
        points.append((r,c))
    area = shoelaceAlgorithm(points)
    area1 = pickTheroem(area, b)
    print(points)
    print(area)
    print(area1+b)# 64294334780659




# part1(data)
part2(data)