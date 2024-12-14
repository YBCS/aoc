from collections import defaultdict, deque


def in_bounds(i, j, data):
    row = len(data)
    col = len(data[0])

    if i < 0 or i >= row or j < 0 or j >= col:
        return False
    return True


def get_points(i, j, visited, points, data, curr_plant):
    # flood fill algorithm
    if not in_bounds(i, j, data):
        return

    if (i, j) in visited:
        return

    plant = data[i][j]
    if plant != curr_plant:
        return

    visited.add((i, j))
    points.append((i, j))
    get_points(i+1, j, visited, points, data, curr_plant)
    get_points(i-1, j, visited, points, data, curr_plant)
    get_points(i, j+1, visited, points, data, curr_plant)
    get_points(i, j-1, visited, points, data, curr_plant)


def get_area(points):
    return len(points)


def get_neighbours(i, j, data, neighbours):
    if in_bounds(i+1, j, data):
        neighbours.append((i+1, j))
    if in_bounds(i-1, j, data):
        neighbours.append((i-1, j))
    if in_bounds(i, j+1, data):
        neighbours.append((i, j+1))
    if in_bounds(i, j-1, data):
        neighbours.append((i, j-1))


def get_perimeter(points, data, curr_plant):
    out = 0
    for i, j in points:
        ans = 4
        neighbours = []
        get_neighbours(i, j, data, neighbours)
        for x, y in neighbours:
            if data[x][y] == curr_plant:
                ans -= 1
        # print(f'for i and j {i,j} the ans is {ans}, curr plant is {curr_plant} neighbours {neighbours}')
        out += ans

    return out

# TODO 
def get_sides(points, data, curr_plant):
    # calculate sides:;::: hoowwww ????
    # Hint: any polygon has as many sides as many corners: #corners == #sides
    corners = 0
    # dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # d u r l
    dirs = [(-1, 0), (0, 1), (1, 0),  (0, -1)]  # u r d l # clockwise
    for i, j in points:
        # case 1 up and left are out of bounds; right and down are the same plant
        for di, dj in dirs:
            points[i+di][j+dj]


def part1(data):
    visited = set()
    ans = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            points = []
            get_points(i, j, visited, points, data, data[i][j])
            if not points:
                continue
            area = get_area(points)
            # perimeter = get_perimeter(points, data, data[i][j])
            sides = get_sides(points, data, data[i][j])
            # ans += area * perimeter
            ans += area * sides
            # print("points ", points)
            # print("area ", area)
            # print("perimeter ", perimeter)
    print('ans is ', ans)
    return ans


def part2():
    pass


if __name__ == "__main__":
    file = "in.txt"
    file = "eg.txt"
    data = open(file, "r").read().split("\n")

    part1(data)
    # part2()
