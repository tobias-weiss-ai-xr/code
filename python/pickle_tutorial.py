# Pickle
import pickle

def outline(func):
    def inner(*args):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args)
        print('-'*20)
    return inner

class Cat():
    def __init__(self, name, age, properties):
        super().__init__()
        self._name = name
        self._age = age
        self._properties = properties

    @outline
    def display(self, msg=''):
        print(msg)
        print(f'{self._name} is a {self._age} years old cat')
        for k, v in self._properties.items():
            print(f'{k} = {v}')

oscar = Cat(name='Oscar', age=11, properties=dict(instrument='piano', sports=['soccer', 'tennis']))

oscar.display('original')

sc = pickle.dumps(oscar)
print(sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(oscar, f)

# deserialize
oscarReloaded = pickle.loads(sc)
oscarReloaded.display('from string')

with open('cat.txt', 'rb') as f:
    oscarReloadedFromFile = pickle.load(f)
oscarReloadedFromFile.display('from disk')