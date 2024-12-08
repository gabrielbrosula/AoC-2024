test = "6-small.txt"
real = "6.txt"

dirs = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]

grid = []
with open(f'./input/6.txt', 'r') as f:
    for line in f:
      row = line.strip('\n')
      grid.append(row)

def row_oob(r):
  return r < 0 or r >= len(grid)

def col_oob(c):
  return c < 0 or c >= len(grid[0])

def walk(r, c):
  idx = 0
  visited = set()
  pr = r
  pc = c

  while True:
    visited.add((pr, pc))
    nr = pr + dirs[idx][0]
    nc = pc + dirs[idx][1]

    #print(f"Visiting {nr}, {nc}")

    if (row_oob(nr) or col_oob(nc)):
      break

    # Turn
    while grid[nr][nc] == '#':
      idx = (idx + 1) % 4
      nr = pr + dirs[idx][0]
      nc = pc + dirs[idx][1]

    pr = nr
    pc = nc


  return visited

def p1():
  rs = 0
  cs = 0

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == '^':
        rs = r
        cs = c

  #print(len(grid) * len(grid[0]))

  return len(walk(rs, cs))

exit_res = (-1, -1, None)

def detectCycle(ob_r, ob_c, sr, sc):
  ob_grid = []

  new_str_chars = []
  old_str = grid[ob_r]
  for i in range(len(old_str)):
      if i == ob_c:
          new_str_chars.append("#")
      else:
        new_str_chars.append(grid[ob_r][i])
  new_str = "".join(new_str_chars)

  for i in range(len(grid)):
      if i == ob_r:
          ob_grid.append(new_str)
      else:
          ob_grid.append(grid[i])

  #print(ob_grid[ob_r][ob_c])

  #print(f"Putting obstacle on {ob_r}, {ob_c}")

  # Tortoise-and-hare (Slow and fast pointers) algorithm for cycle checking
  # Have two walkers, fast and slow
  # If they collide AND are in the same direction there is a cycle

  # Slow
  tpr = sr
  tpc = sc
  t_dir = 0

  # Fast
  hpr = sr
  hpc = sc
  h_dir = 0

  step = 0
  t_tuple = (tpr, tpc, t_dir)
  h_tuple = (hpr, hpc, h_dir)
  while True:
    #print("Step: ", step)
    #print(t_tuple)
    #print(h_tuple)

    if h_tuple == exit_res or t_tuple == exit_res:
      return 0
    elif t_tuple == h_tuple and step != 0:
      return 1

    h_tuple = stepOnce(h_tuple[0], h_tuple[1], h_tuple[2], ob_grid)
    #print("h_tuple:", h_tuple)

    # Hare must take a step before tortoise does!
    if step % 2 == 1:
      t_tuple = stepOnce(t_tuple[0], t_tuple[1], t_tuple[2], ob_grid)
    #print("t_tuple", t_tuple)

    step += 1

def stepOnce(pr, pc, dir_idx, grid):
    nr = pr + dirs[dir_idx][0]
    nc = pc + dirs[dir_idx][1]

    #print(f"Visiting {nr}, {nc}")

    if row_oob(nr) or col_oob(nc):
      # Represents an exit
      return exit_res

    # Turn
    # Account for the case when you turn twice in one step
    while grid[nr][nc] == '#':
      dir_idx = (dir_idx + 1) % 4
      nr = pr + dirs[dir_idx][0]
      nc = pc + dirs[dir_idx][1]

    return (nr, nc, dir_idx)

def p2():
  rs = 0
  cs = 0

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == '^':
        rs = r
        cs = c

  visited = walk(rs, cs)

  # Remove starting point
  visited.remove((rs, cs))

  sum = 0
  #subset = set(x for i, x in enumerate(visited) if i < 2)
  for pos in visited:
    sum += detectCycle(pos[0], pos[1], rs, cs)

  return sum

print(p1())
print(p2())