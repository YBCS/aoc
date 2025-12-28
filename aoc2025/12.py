# YOU ARE NOT GOING TO BELIVE THIS 😭🤣

items = open("inp.txt", "r").read().split("\n\n")

*shapes, spaces = items
spaces = spaces.split("\n")

shapes = [shape.split("\n")[1:] for shape in shapes]

ans = 0
for space in spaces:
    dim, *nums = space.split(":")
    x, y = map(int, dim.split("x"))
    total = x * y
    nums = list(map(int, nums[0].strip().split(" ")))
    boxes = sum(nums)
    area = boxes * 9

    if area <= total:
        ans += 1


print(ans)
