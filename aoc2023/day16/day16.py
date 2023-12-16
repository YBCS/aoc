data = open('input.txt', 'r').read().split('\n')

def part1(grid):
  print('grid is ')
  [print(g) for g in grid]
  energized = set()
  visited_paths = set()

  obst = "|-/\\"

  def is_inbound(i,j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

  def explore(i, j, d):
    # starting from i, j where can it reach
 
    if (i,j,d) in visited_paths: return
    visited_paths.add((i,j,d))
    
    while is_inbound(i,j):
      energized.add((i, j))
      if grid[i][j] in obst:
        if grid[i][j] == "|":
          if d == "l" or d == "r":
            explore(i-1, j, 'u')
            explore(i+1, j, 'd')
            return
        elif grid[i][j] == "-":
          if d == "u" or d == "d":
            explore(i, j-1, 'l')
            explore(i, j+1, 'r')
            return
        elif grid[i][j] == "/":
          if d == "l": d = "d"
          elif d == "r": d = "u"
          elif d == "u": d = "r"
          elif d == "d": d = "l"
        elif grid[i][j] == "\\":
          if d == "l": d = "u"
          elif d == "r": d = "d"
          elif d == "u": d = "l"
          elif d == "d": d = "r"

      if d == "l": j -= 1
      elif d == "r": j += 1
      elif d == "u": i -= 1
      elif d == "d": i += 1

  explore(0,0, 'r')
  print(energized, len(energized))
  print('fin')

def part2(grid):
  # for each edge; which edge gives the most energy
  energized = set()
  visited_paths = set()
  obst = "|-/\\"
  
  def is_inbound(i,j): return 0 <= i < len(grid) and 0 <= j < len(grid[0])

  def explore(i, j, d):
    if (i,j,d) in visited_paths: return
    visited_paths.add((i,j,d))
    
    while is_inbound(i,j):
      energized.add((i, j))
      if grid[i][j] in obst:
        if grid[i][j] == "|":
          if d == "l" or d == "r":
            explore(i-1, j, 'u')
            explore(i+1, j, 'd')
            return
        elif grid[i][j] == "-":
          if d == "u" or d == "d":
            explore(i, j-1, 'l')
            explore(i, j+1, 'r')
            return
        elif grid[i][j] == "/":
          if d == "l": d = "d"
          elif d == "r": d = "u"
          elif d == "u": d = "r"
          elif d == "d": d = "l"
        elif grid[i][j] == "\\":
          if d == "l": d = "u"
          elif d == "r": d = "d"
          elif d == "u": d = "l"
          elif d == "d": d = "r"

      if d == "l": j -= 1
      elif d == "r": j += 1
      elif d == "u": i -= 1
      elif d == "d": i += 1

  ans = 0
  
  # this can be done better
  for i in range(len(grid[0])):
    explore(0,i, 'd')
    ans = max(ans, len(energized))
    print('ans down ', len(energized))
    energized = set()
    visited_paths = set()
  for i in range(len(grid[0])):
    explore(len(grid)-1,i, 'u')
    ans = max(ans, len(energized))
    print('ans up ', len(energized))
    energized = set()
    visited_paths = set()

  for i in range(len(grid)):
    explore(i,0, 'r')
    ans = max(ans, len(energized))
    print('ans right ', len(energized))
    energized = set()
    visited_paths = set()    
  for i in range(len(grid)):
    explore(i, len(grid[0])-1, 'l')
    ans = max(ans, len(energized))
    print('ans left ', len(energized))
    energized = set()
    visited_paths = set()
    
  print('part 2 ans is ', ans) # 9041 # too low; 9064

part2(data)
