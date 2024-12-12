from tqdm import tqdm
from math import log10, floor

day = "11"
test = f"{day}-small"
mini = f"{day}-mini"
real = f"{day}"

input = []

with open(f'./input/{test}.txt', 'r') as f:
    line = f.readline()
    input = [int(x) for x in line.split(' ')]

# Read from input
# Copy into new_list

# Part 2: Use log space
for i in range(len(input)):
    if input[i] != 0:
        input[i] = log10(input[i])
    else:
        input[i] = -1

log_2024 = log10(2024)
def get_num_digits(num):
    if num < 0:
        return 1
    return floor(num) + 1

for i in tqdm(range(6)):
    new_list = []
    print(f"Blink {i+1}")
    for j in range(len(input)):
        lognum = input[j]

        # Using negative 1 to indicate that the previous number is a 0
        if lognum == -1:
            # 0 turns into a 1
            # log(1) = 0
            new_list.append(0)
        else:
            if get_num_digits(lognum) % 2 == 0:
                # Turn to string
                actual = round(pow(10, lognum))
                factor = pow(10, get_num_digits(lognum) - 1)
                lh_num = actual // factor
                rh_num = actual % factor

                print(f"actual: {actual}, factor: {factor}, lh: {lh_num}, rh: {rh_num}")

                # actual = 4412 2351
                # 4412 = actual // 10,000
                # 2351 = actual % 10,000

                new_list.append(log10(lh_num) if lh_num != 0 else -1)
                new_list.append(log10(rh_num) if rh_num != 0 else -1)
            else:
                new_list.append(log_2024 + lognum)
                print(pow(10, log_2024 + lognum))
    input = new_list
    print([round(pow(10, x)) for x in input])
    print(input)

print([get_num_digits(x) for x in input])
print(sum([get_num_digits(x) for x in input]))