from typing import Callable, List, Tuple, TypeVar

T = TypeVar('T')


def foo(x: T) -> T:
    return x


print(foo((1, 2)))
