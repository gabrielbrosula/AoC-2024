from tqdm import tqdm
import math

day = "11"
test = f"{day}-small"
mini = f"{day}-mini"
real = f"{day}"

input = []

with open(f'./input/{real}.txt', 'r') as f:

    line = f.readline()
    input = line.split(' ')

# Read from input
# Copy into new_list
def p1(input):
    for i in tqdm(range(25)):
        new_list = []
        for j in range(len(input)):
            ns = str(int(input[j]))
            if (ns == "0"):
                new_list.append("1")
            elif (len(ns) % 2 == 0):
                mp = len(ns) // 2
                lh = ns[:mp]
                rh = ns[mp:]
                new_list.append(lh)
                new_list.append(rh)
            else:
                new_list.append(str(int(ns) * 2024))

        input = new_list

# Recursion
nums_input = [int(x) for x in input]
def get_num_digits(n):
    if n == 0:
        return 1

    digits = 0
    while n > 0:
        n = n // 10
        digits = digits + 1
    return digits

def p2():
    def solve(x, blinks):
        nd = get_num_digits(x)
        if blinks == 0:
            return 1

        if x == 0:
            return solve(1, blinks - 1)

        if nd % 2 == 0:
            lh = x // pow(10, nd // 2)
            rh = x % pow(10, nd // 2)

            return solve(lh, blinks - 1) + solve(rh, blinks - 1)

        return solve(x * 2024, blinks - 1)

    s = 0
    for x in nums_input:
        res = solve(x, 25)
        s += res

    print(s)

p2()