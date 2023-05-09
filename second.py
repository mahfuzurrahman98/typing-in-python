from typing import Dict, List, Set

my_list: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6]
]

print(my_list)


my_dict: Dict[str, int] = {
    'a': 1,
    'b': 2,
}

print(my_dict)


# create a set of strings
my_set: Set[str] = {
    'a',
    'b',
    'c',
    'd',
    'a',
    'b',
}

print(my_set)