import requests
from requests_toolbelt.multipart.encoder import total_len

first_list = []
second_list = []
with open('./input.txt', 'r') as input_file:
    for line in input_file.readlines():
        nums = line.split(' ')

        first_list.append(int(nums[0].strip()))
        second_list.append(int(nums[-1].strip()))

total_sum = 0
for num in first_list:
    similarity = 0
    for num2 in second_list:
        print(f"{num} / {num2} == {num == num2}")
        if num == num2:
            similarity += 1

    total_sum += num * similarity

print(total_sum)