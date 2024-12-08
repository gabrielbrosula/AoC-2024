rules = []

test_r = "5r-small"
test = "5-small"

real_r = "5r"
real = "5"
with open(f"./input/{real_r}.txt", "r") as f:
    for line in f:
        nums = line.strip("\n").split("|")
        rules.append(nums)

text = []
with open(f"./input/{real}.txt", "r") as f:
    for line in f:
        t = line.strip("\n").split(",")
        text.append(t)


def check(t):
    isSafe = True
    for r in rules:
        if r[0] in t and r[1] in t:
            if not t.index(r[0]) < t.index(r[1]):
                isSafe = False
                break

    return isSafe


def topoSort(rules):
    # rules = edge list

    # Add all nodes with in-degree 0 to the queue
    in_deg = {}
    s = set()
    for r in rules:
        s.add(r[0])
        s.add(r[1])

    for x in s:
        in_deg[x] = 0

    for r in rules:
        in_deg[r[1]] += 1

    # Sort the dictionary by the values
    # Observation: Lower in-degree means that it should come before a higher in-degree number in the list
    sorted_dict = dict(sorted(in_deg.items(), key=lambda item: item[1]))

    return list(sorted_dict.keys())


def getRules(t):
    relevant_rules = []
    for r in rules:
        if r[0] in t and r[1] in t:
            relevant_rules.append(r)

    return relevant_rules


def p1():
    sum = 0
    for t in text:
        if check(t):
            sum += int(t[len(t) // 2])

    print(sum)


def p2():
    sum = 0
    for t in text:
        if not check(t):
            relevant_rules = getRules(t)
            sorted = topoSort(relevant_rules)
            sum += int(sorted[len(sorted) // 2])

    print(sum)


p1()
p2()
