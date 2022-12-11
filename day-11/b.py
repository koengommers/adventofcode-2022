import re
import operator
from functools import reduce

line_pattern = re.compile(r'^([\w\s]+):\s(.*)$')

monkeys = []
items = []
ops = {
    '*': operator.mul,
    '/': operator.floordiv,
    '+': operator.add,
    '-': operator.sub,
}

with open('input') as f:
    monkey = {'count': 0}

    for line in f:
        line = line.strip()
        if line == '':
            monkeys.append(monkey)
            monkey = {'count': 0}
        elif line.startswith('Monkey'):
            pass
        else:
            match = line_pattern.match(line)
            a, b = match.group(1, 2)
            if a == 'Starting items':
                monkey['items'] = []
                for item in [int(x) for x in b.split(', ')]:
                    monkey['items'].append(len(items))
                    items.append(item)
            elif a == 'Operation':
                monkey['operation'] = b 
            elif a == 'Test':
                monkey['test'] = int(b.split().pop())
            elif a == 'If true':
                monkey[True] = int(b.split().pop())
            elif a == 'If false':
                monkey[False] = int(b.split().pop())

    monkeys.append(monkey)

product_of_tests = reduce(lambda a, b: a*b, [m['test'] for m in monkeys])

rounds = 10000
for round in range(rounds):
    for i, monkey in enumerate(monkeys):
        # print(f'Monkey {i}:')
        for item in monkey['items']:
            monkey['count'] += 1
            # print(f'  Monkey inspects an item with a worry level of {item}.')
            x, op, y = monkey['operation'].replace('new = ', '').split()
            op = ops[op]
            x = int(x) if x != 'old' else items[item]
            y = int(y) if y != 'old' else items[item]
            items[item] = op(x, y)
            is_divisible = items[item] % monkey['test'] == 0
            throw_to = monkey[is_divisible]
            monkeys[throw_to]['items'].append(item)
        monkey['items'] = []

    print(f'Round {round+1}')
    counts = [m['count'] for m in monkeys]
    for i, c in enumerate(counts):
        print(f'Monkey {i} inspected items {c} times')
    print()

    items = [i % product_of_tests for i in items]

sorted_counts = sorted(counts, reverse=True)
print(operator.mul(*sorted_counts[:2]))
