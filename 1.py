def main():
    filename = "1.txt"
    left = []
    right = []
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            left.append(int(words[0]))
            right.append(int(words[1]))

    ls = sorted(left)
    rs = sorted(right)
    sum = 0
    ft = {}
    ss = 0
    for i in range(0, len(ls)):
        ln = ls[i]
        sum += abs(ln - rs[i])
        ft[ln] = 0

    for num in rs:
        if num in ft:
            ft[num] += 1

    for k in ft:
        ss += k * ft[k]

    print(sum)
    print(ss)


if __name__ == "__main__":
    main()
