from collections import defaultdict
import os

current_dir = None
dirs = defaultdict(lambda: {'files': [], 'dirs': set()})

with open('input') as f:
    for line in f:
        if line.startswith('$ cd '):
            new_dir = line.strip().split().pop()
            if new_dir == '..':
                current_dir = dirs[current_dir]['parent']
            else:
                if current_dir != None:
                    new_dir = os.path.join(current_dir, new_dir)
                dirs[new_dir]['parent'] = current_dir
                current_dir = new_dir
        elif line.startswith('dir'):
            new_dir = line.split().pop()
            new_dir = os.path.join(current_dir, new_dir)
            dirs[current_dir]['dirs'].add(new_dir)
        elif not line.startswith('$'):
            dirs[current_dir]['files'].append(tuple(line.split()))

dir_sizes = {}
while len(dir_sizes) != len(dirs):
    can_calculate = set([dir for dir in dirs if dirs[dir]['dirs'].issubset(dir_sizes.keys())])
    should_calculate = can_calculate.difference(dir_sizes.keys())
    for dir in should_calculate:
        filesize = sum([int(x[0]) for x in dirs[dir]['files']])
        dirsize = sum(dir_sizes[x] for x in dirs[dir]['dirs'])
        dir_sizes[dir] = filesize + dirsize

space_free = 70000000 - dir_sizes['/']
space_needed = 30000000
should_free_up = space_needed - space_free
possible_dirs = [x for x in dir_sizes.values() if x > should_free_up]
print(sorted(possible_dirs)[0])
