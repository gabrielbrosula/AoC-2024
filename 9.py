import copy

day = "9"
test = f"{day}-small"
mini = f"{day}-mini"
real = f"{day}"

disk_map1 = []
with open(f'./input/{real}.txt', 'r') as f:
    input = f.readline().strip()
    file_idx = 0
    for i, c in enumerate(input):
        is_even = i % 2 == 0
        for j in range(int(c)):
            if i % 2 == 0:
                disk_map1.append(file_idx)
            else:
                disk_map1.append(".")

        if is_even:
            file_idx += 1

def p1():
    left_ptr = disk_map1.index('.')
    right_ptr = len(disk_map1) - 1
    compressed = copy.copy(disk_map1)
    while right_ptr > left_ptr:
        if disk_map1[right_ptr] != '.' and disk_map1[left_ptr] == '.':
            compressed[left_ptr] = disk_map1[right_ptr]
            compressed[right_ptr] = '.'
            left_ptr += 1
            right_ptr -= 1
        elif disk_map1[right_ptr] != '.' and disk_map1[left_ptr] != '.':
            left_ptr += 1
        elif disk_map1[right_ptr] == '.':
            right_ptr -= 1

    checksum = 0
    # Get the input from 0 to the first occurrence of '.', exclusive
    for idx in range(len(compressed[:compressed.index('.')])):
        checksum += idx * compressed[idx]
    print(checksum)

def p2():
    # Index = file_id, blocks[index] = size of the block
    blocks = []
    for i in range(len(input)):
        num = int(input[i])
        if i % 2 == 0:
            blocks.append(num)

    ans = copy.copy(disk_map1)
    # block_idx = file_id that gets written
    for block_idx in range(len(blocks) - 1, -1, -1):
        # block_idx = file_id that gets written
        fs_offset = 0
        fs_window_start = -1
        write_ptr = ans.index('.')
        file_start = disk_map1.index(block_idx)

        # The next free space to write to must be BEFORE when the file actually starts
        while write_ptr < file_start:
            if ans[write_ptr] != '.':
                write_ptr += 1

                # Reset the sliding window
                fs_offset = 0
                fs_window_start = -1
            else:
                fs_offset += 1
                if fs_window_start == -1:
                    fs_window_start = write_ptr

                block_size = blocks[block_idx]
                if fs_offset == block_size:
                    # Write to the free space
                    for j in range(fs_window_start, fs_window_start + block_size):
                        ans[j] = block_idx # Remember: block_idx = file_id

                    # Find the indices where this file was originally written in the disk_map
                    # Replace it with a '.'
                    for j in range(file_start, file_start + block_size):
                        ans[j] = '.'
                    break
                else:
                    write_ptr += 1

    checksum = 0
    for idx in range(len(ans)):
        if ans[idx] != '.':
            checksum += idx * ans[idx]

    print(checksum)

p1()
p2()





