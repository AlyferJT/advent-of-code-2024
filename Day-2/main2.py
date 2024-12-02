level_list = []
with open('./input.txt', 'r') as input_file:
    for line in input_file.readlines():
        num_list = []
        for num in line.split(' '):
            num_list.append(int(num.strip()))
        level_list.append(num_list)


def check_level(input_level, input_last_num, sequence):
    # Check if nums are equal
    if input_level == input_last_num:
        return False

    # Check if continues ascending or descending
    seq = 'asc' if input_level > input_last_num else 'des'
    sequence.append(seq)
    if seq == 'asc' and 'des' in sequence:
        return False
    elif seq == 'des' and 'asc' in sequence:
        return False

    # Check if is safe ups or downs
    if input_level > input_last_num and (input_level - input_last_num) > 3:
        return False
    elif input_level < input_last_num and (input_last_num - input_level) > 3:
        return False

    return True

def check_num_list(n_list):
    last_num = 0
    sequence = []
    safe = True

    for level in n_list:
        if not last_num:
            last_num = level
            continue

        res = check_level(level, last_num, sequence)

        if not res:
            safe = False
            break

        last_num = level

    return safe

safe_level = 0
for level_count in level_list:
    is_safe = check_num_list(level_count)

    if is_safe:
        safe_level += 1
    else:
        temp_list = [num for num in level_count]
        for i in range(0, len(level_count)):
            temp_list.pop(i)
            print(temp_list)

            is_safe = check_num_list(temp_list)

            if is_safe:
                safe_level += 1
                break

            temp_list = [num for num in level_count]

print(safe_level)