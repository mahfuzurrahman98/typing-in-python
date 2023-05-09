from typing import List

vector = List[float]

vectors = List[vector]


def foo(v: vectors) -> vector:
    return v[0]


my_vector = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

print(foo(my_vector))
