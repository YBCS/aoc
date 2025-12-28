# advent of code day 2

data = open("inp.txt", "r").read()

# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# data = "123123123-123123125"

""" part 1
# dont know how to make this fast so
data = data.split(",")
count = 0
for parse in data:
    s, e = parse.split("-")
    s_int, e_int = int(s), int(e)
    for num in range(s_int, e_int + 1):
        size = len(str(num))
        if size % 2 == 0:
            # split in middle and check both side equal or not
            num_str = str(num)
            if num_str[: size // 2] == num_str[size // 2 :]:
                count += num
                print(num_str)


print(count)

"""

""" # part 2


# subdevide until no longer possible 
123123123
9
//2
//3
//4
//5
//6
//7
//8
//9

in first encounter break;

"""

import textwrap

data = data.split(",")
count = 0
for parse in data:
    s, e = parse.split("-")
    s_int, e_int = int(s), int(e)
    for num in range(s_int, e_int + 1):
        size = len(str(num))
        for i in range(1, size + 1):
            if size % i == 0:
                chunks = textwrap.wrap(str(num), size // i)
                if i != 1 and len(set(chunks)) == 1:
                    print(num)
                    count += int(num)
                    break
print(count)
