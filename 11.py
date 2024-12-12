from tqdm import tqdm

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
for i in tqdm(range(75)):
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

print(len(input))