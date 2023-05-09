from typing import Callable, Tuple


def add(x: int, y: int) -> int:
    return x + y


def foo(func: Callable[[int, int], int]) -> int:
    return func(1, 2)


ans = foo(add)
print(ans)


# -----------------------------------------

def foo2() -> Callable[[int, int], int]:
    def sub(x: int, y: int) -> int:
        return x-y
    return sub


new_func = foo2()
print(new_func(1, 2))
