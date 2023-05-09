# create a ariable myName which should be a string and then assign "Mahfuz" to it and then print it, use typehinting
myName: str = "Mahfuz"
print(myName)


def add(a: int, b: int) -> int:
    return a + b

try:
    print(add(1, 2))
except Exception as e:
    print(e)