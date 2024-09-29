
def func(x):
    x=x+3
    return x

def test_func():
    assert func(1) == 4

print(func(3))