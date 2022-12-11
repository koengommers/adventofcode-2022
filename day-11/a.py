import re
import operator

line_pattern = re.compile(r'^([\w\s]+):\s(.*)$')

monkeys = []
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
                monkey['items'] = [int(x) for x in b.split(', ')]
            elif a == 'Operation':
                monkey['operation'] = b 
            elif a == 'Test':
                monkey['test'] = int(b.split().pop())
            elif a == 'If true':
                monkey[True] = int(b.split().pop())
            elif a == 'If false':
                monkey[False] = int(b.split().pop())

    monkeys.append(monkey)

rounds = 20
for round in range(rounds):
    for i, monkey in enumerate(monkeys):
        # print(f'Monkey {i}:')
        for item in monkey['items']:
            monkey['count'] += 1
            # print(f'  Monkey inspects an item with a worry level of {item}.')
            x, op, y = monkey['operation'].replace('new = ', '').split()
            op = ops[op]
            x = int(x) if x != 'old' else item
            y = int(y) if y != 'old' else item
            item = op(x, y)
            # print(f'    Worry level gets {monkey["operation"]} to {item}')
            item = item // 3
            # print(f'    Monkey gets bored with item. Worry level is divided by 3 to {item}')
            is_divisible = item % monkey['test'] == 0
            # print(f'    Current worry level is {"" if is_divisible else "not "}divisible by {monkey["test"]}')
            throw_to = monkey[is_divisible]
            # print(f'    Item with worry level {item} is thrown to monkey {throw_to}.')
            monkeys[throw_to]['items'].append(item)
        monkey['items'] = []

    print(f'Round {round+1}')
    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i}: {", ".join([str(item) for item in monkey["items"]])}')
    print()

counts = [m['count'] for m in monkeys]
for i, c in enumerate(counts):
    print(f'Monkey {i} inspected items {c} times')
print()

sorted_counts = sorted(counts, reverse=True)
print(operator.mul(*sorted_counts[:2]))
