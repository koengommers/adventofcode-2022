from collections import defaultdict
import re

with open('input') as f:
    are_instructions = False
    stacks = []
    instructions = []
    for line in f:
        if line == '\n':
            are_instructions = True
        elif not are_instructions:
            stacks.append(line)
        elif are_instructions:
            instructions.append(line)

stack_indices = stacks.pop().replace('\n', '')
stacks_dict = defaultdict(list)
for index in stack_indices.split():
    line_index = stack_indices.index(index)
    for line in stacks[::-1]:
        if line[line_index] != ' ':
            stacks_dict[index].append(line[line_index])

for instruction in instructions:
    pattern = r'move (\d+) from (\d+) to (\d+)'
    match = re.match(pattern, instruction)
    amount, from_, to = match.group(1, 2, 3)
    stacks_dict[to] += stacks_dict[from_][-int(amount):]
    stacks_dict[from_] = stacks_dict[from_][:-int(amount)]

print(''.join([x[-1] for x in stacks_dict.values()]))
