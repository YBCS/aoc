# this is like the generate subsequence problem

items = open("inp.txt", "r").read().split("\n")


def valid(option, pattern):
    # [(3,), (0, 2), (0, 1)]    # an option eg.
    # [.##.]                    # a pattern eg.
    pattern = list(pattern)[1:-1]
    mask = ["."] * len(pattern)
    for tup in option:
        for item in tup:
            mask[item] = "." if mask[item] == "#" else "#"
    return mask == pattern


def valid2(option, other):
    # [(3,), (0, 2), (0, 1)]    # an option eg.
    # {3,5,4,7}                 # an other eg.

    other = list(map(int, other.strip()[1:-1].split(",")))
    mask = [0] * len(other)
    for tup in option:
        for item in tup:
            mask[item] += 1
    return mask == other


# print(valid([(3,), (0, 2), (0, 1)], "[.##.]"))
# print(valid([(0, 2), (0, 1)], "[.##.]"))
print(valid2([(3,), (0, 2), (0, 1)], "{3,5,4,7}"))


def generate_subsequence(words, i):
    # all subsequence starting from index i
    if i == len(words):
        return [[]]
    rest = generate_subsequence(words, i + 1)
    skip = rest
    take = [[words[i]] + sub for sub in rest]

    return skip + take


def part2(items):
    ### how how how
    ans = 0
    for item in items:
        pattern, *keys, other = item.strip().split(" ")
        keys = [tuple(map(int, key[1:-1].split(","))) for key in keys]
        options = generate_subsequence(keys, 0)
        for option in sorted(options, key=lambda x: len(x)):
            if valid2(option, other):
                ans += len(option)
                break

    print(ans)


def part1(items):
    # 🤣 that's right just forget the fact that you can press a button more than once
    # actully pressing twice will null the input and more than that is just unworthy coz of minimization constraint
    ans = 0
    for item in items:
        pattern, *keys, other = item.strip().split(" ")
        keys = [tuple(map(int, key[1:-1].split(","))) for key in keys]
        options = generate_subsequence(keys, 0)
        for option in sorted(options, key=lambda x: len(x)):
            if valid(option, pattern):
                ans += len(option)
                break

    print(ans)


# print(generate_subsequence([(3), (1, 3), (2), (2, 3), (0, 2), (0, 1)], 0))
# part1(items)
part2(items)
