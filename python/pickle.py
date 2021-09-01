# Pickle

import pickle

def outline(func):
    def inner(*args):
        print('-'*20)
        print(f'Function: {func.__name__')
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
    def display(self):
        pass

oscar = Cat(name='Oscar', age=11, properties=dict(instrument='piano', sports=['soccer', 'baseball']))

sc = pickle.dumps(oscar)
print(sc)