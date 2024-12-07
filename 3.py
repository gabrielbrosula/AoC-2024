import re

s = ""
with open("31.txt", "r") as f:
    lines = f.readlines()
    s = "".join(lines)

res = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", s)

most_recent = 1
p1 = 0
p2 = 0
for op in res:
    if op == "do()":
        most_recent = 1
    elif op == "don't()":
        most_recent = 0
    else:
        fc = op.index(",")
        first = int(op[4:fc])
        second = int(op[fc + 1 : -1])
        p1 += first * second
        p2 += first * second * most_recent

print(p1)
print(p2)
