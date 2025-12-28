items = open("inp.txt", "r").read().split("\n")


junction_boxes = []
for item in items:
    x, y, z = map(int, item.split(","))
    junction_boxes.append((x, y, z))


def euclidean_dist(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))
