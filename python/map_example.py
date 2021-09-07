# map example
# map(func, args*)

people = ['Tom', 'Maximilian', 'Hans']

# old way
counts = []
for p in people:
    counts.append(len(p))
print(f'Old way: {counts}')

# modern way
print(f'New way: {list(map(len,people))}')

firstname = ('Apple', 'Chocolate', 'Fudge', 'Pizza')
lastname = ('Pie', 'Cake', 'Brownies')

def merg(a, b):
    return a + ' ' + b

x = map(merg, firstname, lastname)
print(x)
print(list(x))

# call multiple functions in one map action

def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def doall(func, num):
    return func(num[0], num[1])

f = (add, substract, multiply, divide)
v = [[5, 3]]
n = list(v) * len(f)
print(f'f: {f}, n:{n}')

m =  map(doall, f, n)
print(list(m))