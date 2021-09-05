# map example

people = ['Tom', 'Maximilian', 'Hans']

# old way
counts = []
for p in people:
    counts.append(len(p))
print(f'Old way: {counts}')

# modern way
print(f'New way: {list(map(len,people))}')