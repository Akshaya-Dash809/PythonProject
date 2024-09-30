def test_pass():
    assert 1+1 ==2

def test_fail():
    assert 2+2 == 5


def hi(name):
    return "Hi, {name}".format(**name)

def bye(name):
    return "Bye, {name}".format(**name)

def how_are_you(name):
    return "How are you {name} ?".format(**name)