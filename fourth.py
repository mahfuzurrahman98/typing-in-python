from typing import Any, List, Optional


def foo(output: Optional[List[Any]] = []) -> None:
    pass


foo([1, 2.5, 'x', False, None])
