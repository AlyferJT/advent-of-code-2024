import requests

first_list = []
second_list = []
with open('./input.txt', 'r') as input_file:
    for line in input_file.readlines():
        nums = line.split(' ')

        first_list.append(nums[0].strip())
        second_list.append(nums[-1].strip())

first_list = sorted(first_list)
second_list = sorted(second_list)

final_list = []
for i in range(0, len(first_list)):
    num_1 = int(first_list[i])
    num_2 = int(second_list[i])

    if num_1 > num_2:
        final_list.append(num_1 - num_2)
    else:
        final_list.append(num_2 - num_1)

print(sum(final_list))