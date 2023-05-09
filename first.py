myName: str = "Mahfuz"
print(myName)


def add(a: int, b: int, c: float = 0.5) -> float:
    return a + b + c

try:
    x = add(1, 2, 4)
    print(x)
except Exception as e:
    print(e)