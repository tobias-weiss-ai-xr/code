# Exceptions

# simple decorator
def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner

# try, except and finally

@outline
def test_one(x, y):
    try:
        z = x / y
        print(f'Result: {z}')
    except:
        # catch
        print(f'Something bad happened, x: {x}, y: {y}')
    finally:
        # clean up
        print('Complete')

test_one(5, 0)
test_one(5, 'cats')
test_one(5, 2)

@outline
def test_two(x, y):
    try:
        assert(x > 0)
        assert(y > 0)
    except AssertionError:
        # specific error
        print(f'Failed assertion!')
    except TypeError:
        print(f'Wrong type!')
    except Exception as e:
        # catch
        print(f'Something bad happened, x: {x}, y: {y}, issue: {e}')
    else:
        z = x / y
        print(f'Result: {z}')
        # trusted code
    finally:
        # clean up
        print('Complete')

test_two(5, 0)
test_two(5, 'cats')
test_two(5, 2)

# User defined exception and raising
class CatError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args

@outline
def test_cats(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be an int')
        if qty < 9:
            raise CatError('Must own more than 9 cats')
        print(f'You own {qty} cats')
    except Exception as e:
        print(f'Error: {e.args}')
    finally:
        print(f'Complete')

test_cats(1)
test_cats(10.3)
test_cats(10)