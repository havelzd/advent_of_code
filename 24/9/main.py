import sys
from dataclasses import dataclass


args = sys.argv


def defragment(blocks):
    for file_node_idx in range(len(blocks)-1, 0, -1):
        rid, rsize = blocks[file_node_idx]
        if rid == '.':
            continue
        for free_space_idx in range(file_node_idx):
            lid, lsize = blocks[free_space_idx]

            # print(f"right: {rid} {rsize}, left: {lid} {lsize}")

            if rid != '.' and lid == '.':
                if rsize == lsize:
                    # print("here")
                    blocks[file_node_idx] = ('.', rsize)
                    blocks.pop(free_space_idx)
                    blocks.insert(free_space_idx, (rid, rsize))
                    break
                elif rsize < lsize:
                    blocks[file_node_idx] = ('.', rsize)
                    blocks[free_space_idx] = ('.', lsize - rsize)
                    blocks.insert(free_space_idx, (rid, rsize))
                    break
    return blocks


def get_result_from_blocks(blocks):
    idx = 0
    result = 0
    for b in blocks:
        if b[0] == '.':
            idx += b[1]
        else:
            for i in range(0, b[1]):
                result += idx * b[0]
                idx += 1
    return result


def parse_disk_space(map):
    disk_space = []
    is_file = True
    id = 0
    # print(map)
    for c in map:
        size = int(c)
        for i in range(0, size):
            disk_space.append(id if is_file else '.')
        if is_file:
            id += 1
        is_file = not is_file
    return disk_space


def move_partial_blocks(disk_space):
    # move file block from right to free positions from the left
    # such as 00....111...2 -> 002111.......
    # 1. find the first free position from the left
    # 2. find the first file block from the right
    # 3. move the file block to the free position
    # 4. repeat until no more free positions or file blocks

    left = 0
    right = len(disk_space) - 1
    while left < right:
        while left < right and disk_space[left] != '.':
            left += 1
        while left < right and disk_space[right] == '.':
            right -= 1
        if left < right:
            disk_space[left], disk_space[right] = disk_space[right], disk_space[left]
            left += 1
            right -= 1

    # print(disk_space)


def checksum(disk_space):
    result = 0
    for i in range(0, len(disk_space)):
        if disk_space[i] == '.':
            break
        result += i * disk_space[i]
    print(result)


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        # part 1
        # disk_space = parse_disk_space(line.strip())
        # move_partial_blocks(disk_space)
        # checksum(disk_space)

        # part 2
        blocks = [('.' if i % 2 != 0 else i//2, int(c))
                  for i, c in enumerate(line.strip())]

print(get_result_from_blocks(defragment(blocks)))
