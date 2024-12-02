level_list = []
with open('./input.txt', 'r') as input_file:
    for line in input_file.readlines():
        num_list = []
        for num in line.split(' '):
            num_list.append(int(num.strip()))
        level_list.append(num_list)


safe_level = 0
for level_count in level_list:
    last_num = 0
    sequence = []
    safe = True

    print(level_count)
    for level in level_count:
        if not last_num:
            last_num = level
            continue

        # Check if nums are equal
        if level == last_num:
            safe = False
            break

        # Check if continues ascending or descending
        seq = 'asc' if level > last_num else 'des'
        sequence.append(seq)
        if seq == 'asc' and 'des' in sequence:
            safe = False
            break
        elif seq == 'des' and 'asc' in sequence:
            safe = False
            break

        # Check if is safe ups or downs
        if level > last_num and (level - last_num) > 3:
            safe = False
            break
        elif level < last_num and (last_num - level) > 3:
            safe = False
            break

        last_num = level

    if safe:
        safe_level += 1

print(safe_level)