import itertools

day = "8"
test = f"{day}-small"
real = f"{day}"

grid = []
with open(f'./input/{real}.txt', 'r') as f:
    for line in f:
        grid.append(line.strip())

def row_oob(r):
  return r < 0 or r >= len(grid)

def col_oob(c):
  return c < 0 or c >= len(grid[0])

def within_bounds(pos):
    return not row_oob(pos[0]) and not col_oob(pos[1])

# Find all pairs of nodes
# Map of character to list of positions with the character
ctp_map = dict()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        ch = grid[r][c]
        if ch != '.':
            if ch in ctp_map:
                ctp_map[ch].append((r,c))
            else:
                ctp_map[ch] = [(r,c)]

def p1():
    antinodes = set()
    for ch in ctp_map.keys():
        # Get all combinations of pairs of nodes for character
        pos_list = ctp_map[ch]
        pairs = list(itertools.combinations(pos_list, 2))

        for pair in pairs:
            node_1 = pair[0]
            node_2 = pair[1]

            dr = node_1[0] - node_2[0]
            dc = node_1[1] - node_2[1]

            pa_1 = (node_1[0] + dr, node_1[1] + dc)
            pa_2 = (node_1[0] - dr, node_1[1] - dc)
            pa_3 = (node_2[0] + dr, node_2[1] + dc)
            pa_4 = (node_2[0] - dr, node_2[1] - dc)

            pos_antinodes = [pa_1, pa_2, pa_3, pa_4]

            for pa in pos_antinodes:
                if pa not in pair and within_bounds(pa):
                    antinodes.add(pa)

    return len(antinodes)

def p2():
    antinodes = set()
    for ch in ctp_map.keys():
        # Get all combinations of pairs of nodes for character
        pos_list = ctp_map[ch]
        pairs = list(itertools.combinations(pos_list, 2))

        for pair in pairs:
            node_1 = pair[0]
            node_2 = pair[1]

            dr = node_1[0] - node_2[0]
            dc = node_1[1] - node_2[1]

            # Node 2 should get added by the traversals below
            antinodes.add(node_1)

            # Generate one half of the line (going forward)
            prev_pa = node_1
            while True:
                pa = (prev_pa[0] + dr, prev_pa[1] + dc)

                if within_bounds(pa):
                    antinodes.add(pa)
                    prev_pa = pa
                else:
                    break

            # Generate other half of the line (going backwards)
            prev_pa = node_1
            while within_bounds(prev_pa):
                pa = (prev_pa[0] - dr, prev_pa[1] - dc)

                if within_bounds(pa):
                    antinodes.add(pa)
                    prev_pa = pa
                else:
                    break

    return len(antinodes)
print(p1())
print(p2())