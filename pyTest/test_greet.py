def greet(person):
    return "Hi {name}".format(**person)

def test_greet():
    ak = {"name" : "Akd"}   # Arrange
    greeting = greet(ak)    # Act
    assert greeting == "Hi Akd"  # Assert