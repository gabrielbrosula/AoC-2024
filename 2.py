def isArrAscOrDesc(int_arr):
    asc = sorted(int_arr)
    desc = asc[::-1]

    return (int_arr == asc) or (int_arr == desc)


def adjDiff(int_arr):
    for i in range(1, len(int_arr)):
        prev = int_arr[i - 1]
        cur = int_arr[i]
        diff = abs(cur - prev)
        if not (diff >= 1 and diff <= 3):
            return False

    return True


def bfCheck(int_arr):
    for i in range(0, len(int_arr)):
        newArr = int_arr.copy()
        newArr.pop(i)

        if isArrSafe(newArr):
            return True
    return False


def isArrSafe(int_arr):
    return isArrAscOrDesc(int_arr) and adjDiff(int_arr)


def isArrSafe_p2(int_arr):
    if not isArrSafe(int_arr):
        return bfCheck(int_arr)
    else:
        return True


def main():
    p1 = 0
    p2 = 0
    with open("./input/2.txt", "r") as f:
        for line in f:
            words = line.split()
            int_arr = []
            for w in words:
                int_arr.append(int(w))

            p1 += 1 if isArrSafe(int_arr) else 0
            p2 += 1 if isArrSafe_p2(int_arr) else 0

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
