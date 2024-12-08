dirs = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
]

check = {
    "M": "X",
    "A":"M",
    "S":"A"
}

mat = []

# Searches a single character
def search(r, c):
  num_at_char = 0
  cur_char = mat[r][c]
  for d in dirs:
    nr = r + d[0]
    nc = c + d[1]
    res = dfs(nr, nc, d, cur_char)

    num_at_char += res

  return num_at_char

def row_oob(r):
  return r < 0 or r >= len(mat)

def col_oob(c):
  return c < 0 or c >= len(mat[0])

def dfs(r, c, dir, prev_char):
  # OOB handling
  if row_oob(r) or col_oob(c):
    return 0
  else:
    cur_char = mat[r][c]
    if prev_char == "A" and cur_char == "S":
      return 1

    if cur_char in check.keys() and check[cur_char] == prev_char:
      return dfs(r + dir[0], c + dir[1], dir, cur_char)

    return 0

with open('./input/4.txt', 'r') as f:
    for line in f:
      mat.append(list(line.strip('\n')))

def p1():
  sum = 0
  for r in range(len(mat)):
    for c in range(len(mat[r])):
      if mat[r][c] == "X":
        sum += search(r, c)

  return sum

def p2():
    sum = 0
    for r in range(1, len(mat) - 1):
        for c in range(1, len(mat[0]) - 1):
            if mat[r][c] == "A":
                if (mat[r - 1][c - 1] == "M" and mat[r + 1][c + 1] == "S") or (mat[r - 1][c - 1] == "S" and mat[r + 1][c + 1] == "M"):
                    if (mat[r + 1][c - 1] == "M" and mat[r - 1][c + 1] == "S") or (mat[r + 1][c - 1] == "S" and mat[r - 1][c + 1] == "M"):
                        sum += 1

    return sum


print(p1())
print(p2())

