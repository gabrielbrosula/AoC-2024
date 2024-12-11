day = "10"
test = f"{day}-small"
mini = f"{day}-mini"
real = f"{day}"

dirs = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]


mat = []
with open(f'./input/{real}.txt', 'r') as f:
    for line in f:
        mat.append(line.strip())

def row_oob(r):
  return r < 0 or r >= len(mat)

def col_oob(c):
  return c < 0 or c >= len(mat[0])

# Part 1: It is not the number of paths. It is the number of distinct nines you can reach from a zero.
# DFS
visited_nines = set()
def dfs_p1(r, c, prev_num, visited):
    if row_oob(r) or col_oob(c):
        return 0

    cur_num = int(mat[r][c])
    sum = 0
    if prev_num == cur_num - 1:
        if cur_num == 9 and (r,c) not in visited_nines:
            visited_nines.add((r,c))
            return 1
        else:
            for idx, d in enumerate(dirs):
                nr = r + d[0]
                nc = c + d[1]
                res = dfs_p1(nr, nc, cur_num, visited)
                sum += res
    return sum

# Part 2: Count number of distinct paths
def dfs_p2(r, c, prev_num):
    if row_oob(r) or col_oob(c):
        return 0

    cur_num = int(mat[r][c])
    sum = 0
    if prev_num == cur_num - 1:
        if cur_num == 9:
            return 1
        else:
            for idx, d in enumerate(dirs):
                nr = r + d[0]
                nc = c + d[1]

                res = dfs_p2(nr, nc, cur_num)
                sum += res
    return sum

def base():
    p1 = 0
    p2 = 0
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == "0":
                s1 = []
                p1 += dfs_p1(r, c, -1, s1)
                visited_nines.clear() # Clear set of visited_nines

                p2 += dfs_p2(r, c, -1)
    return p1, p2

p1, p2 = base()
print(p1)
print(p2)