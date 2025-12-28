items = open("inp.txt", "r").read().split("\n")


def part1(data):
    sep = False
    fresh = 0
    ranges = []
    for item in items:
        if sep:
            num = int(item)
            for a, b in ranges:
                if num <= b and num >= a:
                    fresh += 1
                    break
        else:
            if not item:
                sep = True
                continue
            a, b = item.split("-")
            ranges.append((int(a), int(b)))

    print(fresh)


# bruteforce (does not work)
def part2brute(items):
    sep = False
    ranges = []
    for item in items:
        if sep:
            break
        else:
            if not item:
                break
            a, b = item.split("-")
            ranges.append((int(a), int(b)))

    print(sorted(ranges))


def part2(items):
    sep = False
    ranges = []
    for item in items:
        if sep:
            break
        else:
            if not item:
                break
            a, b = item.split("-")
            ranges.append((int(a), int(b)))

    ranges.sort()
    size = len(ranges)
    atleast_one_merge = False
    while True:
        merged_ranges = []
        if atleast_one_merge:
            break
        for i in range(size):
            if not merged_ranges:
                merged_ranges.append(ranges[i])

            else:
                prev_a, prev_b = merged_ranges[-1]
                curr_a, curr_b = ranges[i]

                # check overlap
                if (
                    (prev_a <= curr_b and prev_a >= curr_a)
                    or (prev_b <= curr_b and prev_b >= curr_a)
                    or (curr_a <= prev_b and curr_a >= prev_a)
                    or (curr_b <= prev_b and curr_b >= prev_a)
                ):
                    atleast_one_merge = True
                    merged_ranges.pop()
                    merged_ranges.append((min(prev_a, curr_a), max(prev_b, curr_b)))
                else:
                    merged_ranges.append(ranges[i])

        ranges = merged_ranges

    ans = 0
    for a, b in ranges:
        ans += b - a + 1
    print(ans)


part2(items)
