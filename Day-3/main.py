import re

pattern = r"mul\((\d+),(\d+)\)"
with open('./input.txt', 'r') as input_file:
    text = input_file.read()

matches = [(int(a), int(b)) for a, b in re.findall(pattern, text)]

accumulator = 0
for n_mul in matches:
    accumulator += n_mul[0] * n_mul[1]

print(accumulator)